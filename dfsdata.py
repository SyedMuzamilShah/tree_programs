class TableNode:
    def __init__(self, open_node, closed_node):
        self.open_node = open_node
        self.closed_node = closed_node

def dfs_data_driven(tree, start_node, goal_node):
    open_nodes = [start_node]
    closed_nodes = ["∅"]
    data = [TableNode(open_node=[start_node], closed_node=["∅"])]

    while open_nodes:
        current_node = open_nodes.pop(0)
        if closed_nodes == ["∅"]:
            closed_nodes = [current_node]
        else:
            closed_nodes.append(current_node)
        
        if current_node == goal_node:
            # data.append(TableNode(open_node=[], closed_node=closed_nodes.copy()))
            return data
        
        children = tree.get(current_node, [])
        for child in reversed(children):  # reversed to maintain the order in the stack for DFS
            if child not in closed_nodes and child not in open_nodes:
                open_nodes.insert(0, child)

        data.append(TableNode(open_node=open_nodes.copy(), closed_node=closed_nodes.copy()))
    
    return data

# # Define the tree
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

# # Define the start node
# start_node = "B"
# goal_node = "H"

# # Execute data-driven DFS
# data = dfs_data_driven(tree, start_node, goal_node)

# # Print the results
# for i, entry in enumerate(data):
#     print(f"Step {i}: Open nodes = {entry.open_node}, Closed nodes = {entry.closed_node}")
