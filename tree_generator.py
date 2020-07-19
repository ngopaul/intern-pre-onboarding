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
    start_node = ["start", "start", "start", "Which category would you like to begin exploring?", 0, ["culture0"]]
    culture0_node = ["culture0", "culture", "resource", "https://www.amazon.jobs/en/principles", 0, ["culture1"]]
    culture1_node = ["culture1", "culture", "question", ["Which leadership principle involves starting with the customer and working backwards?", "customer obsession"], 100, ["end"]]
    end_node = ["end", "end", "end", "Congratulations on finishing the course!", 0, []]
    all_nodes = [start_node, culture0_node, culture1_node, end_node]
    with open("tree.txt", "w") as f:
        f.write(str(all_nodes))
