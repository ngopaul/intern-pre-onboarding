""" Nodes.
node = [
    name of node: str which grammatically fits the statement f"You are at {name}",
    category: str which is just an arbitrary grouping scheme,
    type: "question" | "resource" | "start" | "end",
    data: data which is handled differently depending on the type. usually of type str or list<str>.
    exp: int,
    children: List<str> (list of children names)
]

All nodes require all parents to have been completed in order to access them.
"""

if __name__ == "__main__":
    start_node = ["start", "start", "start", "Which category would you like to begin exploring?", 0, ["culture0", "bookmarks0", 
"technical0"]]
    culture0_node = ["culture0", "culture", "resource", "Take a look at the leadership principles at tinyurl.com/alexa-intern-1", 0, ["culture1"]]
    culture1_node = ["culture1", "culture", "question", ["Which leadership principle involves starting with the customer and working backwards?", "customer obsession"], 100, ["culture2"]]
    culture2_node = ["culture2", "culture", "resource", "Take a look at the 2016 letter to shareholders. Go to tinyurl.com/alexa-intern-2", 0, ["culture3"]]
    culture3_node = ["culture3", "culture", "question", ["At amazon, it is always day what?", "one"], 100, ["culture4"]]
    culture4_node = ["culture4", "culture", "resource", "Read how door desks came to be. Go to tinyurl.com/alexa-intern-3", 0, ["culture5"]]
    culture5_node = ["culture5", "culture", "question", ["What leadership principle do door desks represent?", "frugality"], 100, ["culture6"]]
    culture6_node = ["culture6", "culture", "resource", "Read about amazon affinity groups at the link tinyurl.com/alexa-intern-5", 0, ["end"]]
    
    bookmarks0_node = ["bookmarks0", "bookmarks", "resource", "Bookmark this link: it.amazon.com for I T help.", 0, ["bookmarks1"]]
    bookmarks1_node = ["bookmarks1", "bookmarks", "resource", "Bookmark security.a2z.com with the number 2. This site is for security breach reporting. You cannot access this site outside of the amazon network.", 0, ["bookmarks2"]]
    bookmarks2_node = ["bookmarks2", "bookmarks", "resource", "You are halfway done with bookmarks! Bookmark atoz.amazon.work for information about perks, pay, and contact information. You will be able to access this site after creating your amazon login credentials on Day One.", 0, ["bookmarks3"]]
    bookmarks3_node = ["bookmarks3", "bookmarks", "resource", "Bookmark phonetool.amazon.com. This is Amazon's internal directory of employees which you can only access on the Amazon network.", 0, ["end"]]
    
    technical0_node = ["technical0", "technical", "resource", "Review terminal commands at this URL. tinyurl.com/alexa-intern-4", 0, ["technical1"]]
    technical1_node = ["technical1", "technical", "question", ["Which linux command displays a manual for a given command name?", "man"], 100, ["technical2"]]
    technical2_node = ["technical2", "technical", "resource", "AWS is a huge service that Amazon provides to customers big and small. Here is a video intro about it: tinyurl.com/alexa-intern-6", 0, ["technical3"]]
    technical3_node = ["technical3", "technical", "question", ["What does the W in AWS stand for?", "web"], 100, ["end"]]
    
    end_node = ["end", "end", "end", "Congratulations on finishing the course!", 0, []]
    all_nodes = [start_node, culture0_node, culture1_node, culture2_node, culture3_node, culture4_node, culture5_node, culture6_node, bookmarks0_node, bookmarks1_node, bookmarks2_node, bookmarks3_node, technical0_node, technical1_node, technical2_node, technical3_node, end_node]
    with open("tree.txt", "w") as f:
        f.write(str(all_nodes))
