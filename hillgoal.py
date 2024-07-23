class TableNode:
    def __init__(self, open_node, closed_node):
        self.open_node = open_node  # Format: [node, heuristic, parent]
        self.closed_node = closed_node  # Format: [[node, heuristic, parent], ...]

def goal_driven_hill_climbing(tree, start_node, goal_node, heuristics):
    open_nodes = [[goal_node, heuristics[goal_node], "∅"]]
    closed_nodes = []  # Start with an empty list, not ["∅"]
    data = [TableNode(open_node=open_nodes[0], closed_node=["∅"])]  # Initial closed_node list contains "∅"
    
    while open_nodes:
        # Sort the open nodes by heuristic value
        open_nodes.sort(key=lambda x: x[1])
        current_node = open_nodes.pop(0)
        
        if current_node[0] == start_node:
            # closed_nodes.append(current_node)
            # data.append(TableNode(open_node=[], closed_node=closed_nodes.copy()))
            return data
        
        closed_nodes.append(current_node)
        
        # Find the parent nodes of the current node
        parent_nodes = []
        for node, children in tree.items():
            if current_node[0] in children:
                parent_nodes.append(node)
        
        next_open_nodes = []
        for parent in parent_nodes:
            if not any(c[0] == parent for c in closed_nodes):
                next_open_nodes.append([parent, heuristics[parent], current_node[0]])
        
        if next_open_nodes:
            next_open_nodes.sort(key=lambda x: x[1])
            next_open_node = next_open_nodes[0]
            open_nodes = [next_open_node]
            closed_nodes.extend(next_open_nodes[1:])
        else:
            open_nodes = []
        
        data.append(TableNode(open_node=open_nodes[0] if open_nodes else [], closed_node=closed_nodes.copy()))
    
    return data

# Define the tree
tree = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["E", "G"],
    "D": ["E", "F", "G"],
    "E": ["H", "I"],
    "F": ["I"],
    "G": ["H", "I"],
    "H": [],
    "I": [],
}

# Heuristic values for each node
heuristics = {
    "A": 10,
    "B": 9,
    "C": 5,
    "D": 8,
    "E": 4,
    "F": 2,
    "G": 6,
    "H": 2,
    "I": 8,
}

# Define start and goal nodes
start_node = "A"
goal_node = "H"

# Execute goal-driven hill climbing
data = goal_driven_hill_climbing(tree, start_node, goal_node, heuristics)

# Print the results
for i, entry in enumerate(data):
    if entry.open_node:
        print(f"Step {i}: Open nodes = {entry.open_node}, Closed nodes = {entry.closed_node}")
    # else:
        # print(f"Step {i}: Open nodes = [], Closed nodes = {entry.closed_node}")
