from typing import Union
return_type = Union[dict, list]

def take_input_graph(isHillClimbing = False) -> return_type:
    tree = {}
    isHillClimbingValue = {}

    while True:
        node = input("Enter a node for exit enter done : ")
        if node.lower() == "done":
            break

        node_child = input(f"Enter a node {node} child with comman separated ").split(",")

        if node in tree:
            print(f"Node {node} already has children defined. Skipping.")
            continue

        tree[node] = node_child
        if (isHillClimbing):
            value = eval(input(f"Enter {node} heuristics value : "))
            isHillClimbingValue[node] = value

        node_child_copy = node_child.copy()
        while node_child_copy:
            
            sub_node_index_value = node_child_copy.pop(0)
            if (sub_node_index_value[0] in tree):
                continue
            node_child_sub = input(f"Enter a node {sub_node_index_value[0]} child with comman separated ").split(",")
            if (len(node_child_sub[0]) == 0):
                node_child_sub = []

            node_child_copy = node_child_copy + node_child_sub
            tree[sub_node_index_value] = node_child_sub
            if (isHillClimbing):
                value = eval(input(f"Enter {sub_node_index_value} heuristics value : "))
                isHillClimbingValue[sub_node_index_value] = value
    if (isHillClimbing):
        return [tree, isHillClimbingValue]
    return tree
