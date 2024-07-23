class TableNode:
    def __init__(self, open_node, closed_node):
        self.open_node = open_node
        self.closed_node = closed_node

def invert_tree(tree):
    inverted_tree = {}
    for parent, children in tree.items():
        for child in children:
            if child not in inverted_tree:
                inverted_tree[child] = []
            inverted_tree[child].append(parent)
    return inverted_tree

def goal_driven_bfs(tree, start_node, goal_node):
    inverted_tree = invert_tree(tree)
    open_nodes = [goal_node]
    closed_nodes = ["∅"]
    data = [TableNode(open_node=[goal_node], closed_node=["∅"])]

    while open_nodes:
        current_node = open_nodes.pop(0)
        if closed_nodes == ["∅"]:
            closed_nodes = [current_node]
        else:
            closed_nodes.append(current_node)
        
        if current_node == start_node:
            # data.append(TableNode(open_node=[], closed_node=closed_nodes.copy()))
            return data

        parents = inverted_tree.get(current_node, [])
        for parent in parents:
            if parent not in closed_nodes and parent not in open_nodes:
                open_nodes.append(parent)

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

# # Define start and goal nodes
# start_node = "A"
# goal_node = "H"

# # Execute goal-driven BFS
# data = goal_driven_bfs(tree, start_node, goal_node)

# # Print the results
# for i, entry in enumerate(data):
#     print(f"Step {i}: Open nodes = {entry.open_node}, Closed nodes = {entry.closed_node}")
