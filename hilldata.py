# Step 0: Open nodes = ['A', 10, '∅'], Closed nodes = ['∅']
# Step 1: Open nodes = ['C', 5, 'A'], Closed nodes = [["A", 10, "∅"], ["B", 9, "A"], ["D", 8, "A"]]
# Step 2: Open nodes = ['E', 4, 'C'], Closed nodes = [["A", 10, "∅"], ["B", 9, "A"], ["D", 8, "A"],["G", 6, "C"], ["C", 5, "A"]]
# Step 3: Open nodes = ['H', 2, 'E'], Closed nodes = [["A", 10, "∅"], ["B", 9, "A"], ["D", 8, "A"],["G", 6, "C"], ["C", 5, "A"],
#                                                     ["E", 4, "C"], ["I", 8, "E"]]
class TableNode:
    def __init__(self, open_node, closed_node):
        self.open_node = open_node  # Format: [node, heuristic, parent]
        self.closed_node = closed_node  # Format: [[node, heuristic, parent], ...]

def hill_climbing_data_driven(tree, start_node, goal_node, heuristics):
    open_nodes = [[start_node, heuristics[start_node], "∅"]]
    closed_nodes = []  # Start with an empty list, not ["∅"]
    data = [TableNode(open_node=open_nodes[0], closed_node=["∅"])]  # Initial closed_node list contains "∅"
    
    while open_nodes:
        # Sort the open nodes by heuristic value
        open_nodes.sort(key=lambda x: x[1])
        current_node = open_nodes.pop(0)
        
        if current_node[0] == goal_node:
            print(data[0].closed_node)
            # closed_nodes.append(current_node)
            # data.append(TableNode(open_node=[], closed_node=closed_nodes.copy()))
            return data
        
        closed_nodes.append(current_node)
        
        children = tree.get(current_node[0], [])
        next_open_nodes = []
        for child in children:
            if not any(c[0] == child for c in closed_nodes):
                next_open_nodes.append([child, heuristics[child], current_node[0]])
        
        if next_open_nodes:
            next_open_nodes.sort(key=lambda x: x[1])
            next_open_node = next_open_nodes[0]
            open_nodes = [next_open_node]
            closed_nodes.extend(next_open_nodes[1:])
        else:
            open_nodes = []
        
        data.append(TableNode(open_node=open_nodes[0] if open_nodes else [], closed_node=closed_nodes.copy()))
    print(data)
    return data

# # Define the tree
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
    "J": [],
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
    "J": 0  # Assuming J is not connected and has a heuristic value
}

# # Define start and goal nodes
start_node = "A"
goal_node = "H"

# # Execute hill-climbing
data = hill_climbing_data_driven(tree, start_node, goal_node, heuristics)

# # Print the results
for i, entry in enumerate(data):
    if entry.open_node:
        print(f"Step {i}: Open nodes = {entry.open_node}, Closed nodes = {entry.closed_node}")
    # else:
        # print(f"Step {i}: Open nodes = [], Closed nodes = {entry.closed_node}")
