import logging
import os
import boto3 from botocore.exceptions
import ClientError
def create_presigned_url(object_name):
    """Generate a presigned URL to share an S3 object with a capped expiration of 60 seconds
    :param object_name: string
    return: Presigned URL as string. If error, returns None.
    """
    s3_client = boto3.client('s3',
                             region_name=os.environ.get('S3_PERSISTENCE_REGION'),
                             config=boto3.session.Config(signature_version='s3v4',s3={'addressing_style': 'path'}))
    try:
        bucket_name = os.environ.get('S3_PERSISTENCE_BUCKET')
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=60*1)
    except ClientError as e:
        logging.error(e)
        return None
    # The response contains the presigned URL
    return response

def find_next_nodes(tree_content, tree_status):
    """Find the next nodes (for which all parents have been completed) based on the tree_content
    and tree_status.
    Behavior:
        NON-DESTRUCTIVE
        CREATE NEW REFERENCES (no pointers to objects in the arguments, recursively or otherwise)
    Args:
        tree_content: List<Node>
            A Node is a python list where Node[0] is the name of the node, a unique str.
            Node[-1]: List<str>, where each string is the name of a Node which is a child of this Node
            Node[1:-1]: reserved for data
            EVERY TREE IS A DAG.
        tree_status: List<int>
            Each value in the tree_status represents whether or not the corresponding Node
            in tree_content has been completed or not. 1 for completed, 0 for not completed.
    Returns:
        next_nodes: List<Node>
            A list of the Nodes which are the next Nodes to complete. Every Node is a next_node if
            all of its parent Nodes have been completed, or it has no parent Nodes.
    """
    if not len(tree_content):
        return []
    
    result, parent_status, children = [], [1], [tree_content[0][0]]
    for i in range(len(tree_content)):
        current_node = tree_content[i]
        current_node_name = current_node[0]
        current_node_children = current_node[-1]
        if current_node_name in children:
            parent_index = children.index(current_node_name)
            if parent_status[parent_index]:
                if not tree_status[i]:
                    result.append(current_node)
            del parent_status[parent_index]
            children.remove(current_node_name)
            children.extend(current_node_children)
            parent_status.extend([tree_status[i]] * len(current_node_children))
    return result
    
#     if testOverride == 2:
#         return [
#             ['culture1', 'culture', 'question',
#                 ['Which leadership principle involves starting with the customer and working backwards?', 'customer obsession'],
#                 100, ['end']
#             ]
#         ]
#     elif testOverride == 3:
#         return [
#             ['end', 'end', 'end', 'Congratulations on finishing the course!', 0, []]
#         ]
#     return [['culture0', 'culture', 'resource', 'https://www.amazon.jobs/en/principles', 0, ['culture1']]]

def get_choices_prompt(session_attributes, tree_content):
    next_nodes_string = ""
    for next_node in session_attributes['next_nodes']:
        next_nodes_string += next_node[1] + ". " # add all of the categories
        
    if session_attributes['selected_node'] == 0:
        # have not selected a node (THIS DOES NOT MEAN SELECTING NODE 0)
        speech_text = "Choose one of the following topics. " + next_nodes_string
        reprompt = "Say one of these categories: " + next_nodes_string + "Or say quit to exit. "
    elif session_attributes['selected_node'] == -1:
        # completed the game
        speech_text = (
            "You have completed the game. Please note the following code to receive "
            "your phone tool icon. Say yes for the code, or no to exit.")
        reprompt = ("Say yes to receive a completion code, or no to exit.")
    else:
        # you are in the middle of the game, and have selected a node
        selected_node = tree_content[session_attributes['selected_node']]
        node_type = selected_node[2]
        if node_type == 'question':
            speech_text = (
                "Here is a {} question. {} "
                "Say Answer Question followed by the answer, "
                "Repeat Question, or Select a category.".format(selected_node[1], selected_node[3][0])
                )
        elif node_type == 'resource':
            speech_text = (
                "Here is a {} resource. {}. "
                "Say Next Node, Repeat Resource, or Select a category.".format(selected_node[1], selected_node[3]))
        else:
            speech_text = (
                "You are at a {} node of type {}.".format(selected_node[1], selected_node[2]))
        reprompt = speech_text
    return speech_text, reprompt
