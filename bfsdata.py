
class TableNode:
    def __init__(self, open_node, closed_node):
        self.open_node = open_node
        self.closed_node = closed_node

def bfs_data_driven(tree, start_node, goal_node):

    open_nodes = [start_node]
    closed_nodes = ["∅"]  # Initialize with ∅ as the first closed node
    data = [TableNode(open_node=[start_node], closed_node=["∅"])]

    while open_nodes:
        current_node = open_nodes.pop(0)

        # Remove the "∅" from list
        if closed_nodes == ["∅"]:
            closed_nodes = [current_node]
        else:
            closed_nodes.append(current_node)
        # B = H
        if current_node == goal_node:
            # data.append(TableNode(open_node=[], closed_node=closed_nodes.copy()))
            return data

        children = tree.get(current_node, [])
        for child in children:
            if child not in closed_nodes and child not in open_nodes:
                open_nodes.append(child)

        data.append(TableNode(open_node=open_nodes.copy(), closed_node=closed_nodes.copy()))
    
    # print("REACHED IN TO FIANL")
    # print_table(data=data)
    return data


tree = {
    "S": ["A", "H"],
    "A": ["B", "C"],
    "B": ["D", "E"],
    "D" : [],
    "E" : [],
    "C": ["G"],
    "H": ["I", "J"],
    "I": ["K"],
    "J": []

}

# Define start and goal nodes
start_node = "S"
goal_node = "G"

# Execute BFS_data_driven
data = bfs_data_driven(tree, start_node, goal_node)

for i, entry in enumerate(data):
    print(f"Step {i}: Open nodes = {entry.open_node}, Closed nodes = {entry.closed_node}")



# Define the tree
# tree = {
#     "A": ["D", "E"],
#     "B": ["D", "F", "G"],
#     "C": ["F"],
#     "D": ["I", "J"],
#     "E": ["H"],
#     "F": ["H", "J"],
#     "G": ["I"],
#     "H": [],
#     "I": [],
#     "J": [],
# }