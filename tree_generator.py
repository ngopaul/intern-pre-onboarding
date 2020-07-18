""" Nodes.
node = [
    name of node: str which grammatically fits the statement f"You are at {name}",
    type: "question" | "resource" | "start" | "end",
    data: str which is either the question (if type question) or the link (if type resource),
    exp: int,
    extra data: List<str> extra data to consume to add additional features,
    children: List<str> (list of children names)
]

All nodes require all parents to have been completed in order to access them.
"""

if __name__ == "__main__":
    start_node = ["start", "start", "Which category would you like to begin exploring?", 0, [], ["culture0"]]
    culture0_node = ["culture0", "resource", "https://www.amazon.jobs/en/principles", 0, [], ["culture1"]]
    culture1_node = ["culture0", "question", "Which leadership principle involves starting with the customer and working backwards?", 100, ["Incorrect. Try again.", "Correct."], ["end"]]
    end_node = ["end", "end", "Congratulations on finishing the course!", 0, [], []]
    all_nodes = [start_node, culture0_node, culture1_node, end_node]
    with open("tree.txt", "w") as f:
        f.write(str(all_nodes))