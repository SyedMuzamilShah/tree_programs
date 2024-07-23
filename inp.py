def take_tree_input():
    tree = {}
    nodes_with_children = set()

    while True:
        node = input("Enter a node (or type 'done' to finish): ")
        if node.lower() == 'done':
            break
        
        if node in nodes_with_children:
            print(f"Node {node} already has children defined. Skipping.")
            continue

        children = input(f"Enter the children of node {node} as a comma-separated list (or leave blank if no children): ")
        if children:
            child_nodes = [child.strip() for child in children.split(",")]
            tree[node] = child_nodes
            nodes_with_children.add(node)
            for child in child_nodes:
                if child not in tree:
                    tree[child] = []
        else:
            tree[node] = []

    return tree

# Take tree input from user
tree = take_tree_input()
print("Tree structure:", tree)
