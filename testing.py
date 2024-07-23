class TableNode:
    def __init__(self, open_node, closed_node):
        self.open_node = open_node
        self.closed_node = closed_node

def bfs_data_driven(tree, start_node, goal_node):
    open_nodes = [start_node]
    closed_nodes = ["∅"]  # Initialize with ∅ as the first closed node
    data = [TableNode(open_node=[start_node], closed_node=["∅"])]
    parent = {start_node: None}  # Dictionary to store the parent of each node
    while open_nodes:
        current_node = open_nodes.pop(0)

        # Remove the "∅" from list
        if closed_nodes == ["∅"]:
            closed_nodes = [current_node]
        else:
            closed_nodes.append(current_node)
        
        if current_node == goal_node:
            return data, parent

        children = tree.get(current_node, [])
        for child in children:
            if child not in closed_nodes and child not in open_nodes:
                open_nodes.append(child)
                parent[child] = current_node  # Update the parent dictionary

        data.append(TableNode(open_node=open_nodes.copy(), closed_node=closed_nodes.copy()))
    
    return data, parent

def get_solution_path(parent, start_node, goal_node):
    path = []
    current_node = goal_node
    while current_node is not None:
        path.append(current_node)
        current_node = parent[current_node]
    path.reverse()  # Reverse the path to get it from start_node to goal_node
    return path

tree = {
    "S": ["A", "H"],
    "A": ["B", "C"],
    "B": ["D", "E"],
    "D": [],
    "E": [],
    "C": ["G"],
    "H": ["I", "J"],
    "I": ["K"],
    "J": []
}

tree = {
    "A": ["D", "E"],
    "B": ["D", "F", "G"],
    "C": ["F"],
    "D": ["I", "J"],
    "E": ["H"],
    "F": ["H", "J"],
    "G": ["I"],
    "H": [],
    "I": [],
    "J": [],
}

# Define start and goal nodes
# start_node = "S"
start_node = "B"
goal_node = "H"
# goal_node = "G"

# Execute BFS_data_driven
data, parent = bfs_data_driven(tree, start_node, goal_node)

for i, entry in enumerate(data):
    print(f"Step {i}: Open nodes = {entry.open_node}, Closed nodes = {entry.closed_node}")

# Get and print the solution path
solution_path = get_solution_path(parent, start_node, goal_node)
print("Solution path:", " -> ".join(solution_path))
