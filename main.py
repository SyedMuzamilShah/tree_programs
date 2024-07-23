from bfsdata import bfs_data_driven
from bfsgoal import goal_driven_bfs
from dfsdata import dfs_data_driven
from dfsgoal import goal_driven_dfs
from hilldata import hill_climbing_data_driven
from hillgoal import goal_driven_hill_climbing
from input_take import take_input_graph
from printtable import PrintGraphTable
class TreeClass:
    def __init__(self, tree, start_node, goal_node, isHillClimbing = False):
        self.tree = tree
        self.start_node = start_node
        self.goal_node = goal_node
        self.isHillClimbing = isHillClimbing

def hill(obj : TreeClass):
    # [tree, isHillClimbingValue]

    table = hill_climbing_data_driven(tree=obj.tree[0], start_node=obj.start_node, goal_node=obj.goal_node, heuristics=obj.tree[1])

    # Hill Datadriven
    objTable = PrintGraphTable(table, isHeuristics=True)

    print('\n' +"--"*30 + "Data driven"+ "--"*30 + '\n' ) 
    objTable.print_table()
    
    # # Hill Goaldriven
    table = goal_driven_hill_climbing(tree=obj.tree[0], start_node=obj.start_node, goal_node=obj.goal_node, heuristics=obj.tree[1])
    objTable = PrintGraphTable(table, isHeuristics=True)
    print('\n' +"--"*30 + "Goal driven"+ "--"*30 + '\n' ) 
    objTable.print_table()





def bfs_data_goal(obj : TreeClass):
    table = bfs_data_driven(tree=obj.tree, start_node=obj.start_node, goal_node=obj.goal_node)

    # BFS Datadriven
    objTable = PrintGraphTable(table)
    
    print('\n' +"--"*30 + " bfs Data driven"+ "--"*30 + '\n' ) 
    objTable.print_table()

    # BFS Goaldriven
    table = goal_driven_bfs(tree=obj.tree, start_node=obj.start_node, goal_node=obj.goal_node)
    objTable = PrintGraphTable(table)
    print('\n' +"--"*30 + "bfs Goal driven"+ "--"*30 + '\n' ) 
    objTable.print_table()


def dfs_data_goal(obj : TreeClass):
    table = dfs_data_driven(tree=obj.tree, start_node=obj.start_node, goal_node=obj.goal_node)

    # BFS Datadriven
    objTable = PrintGraphTable(table)

    print('\n' +"--"*30 + "Data driven"+ "--"*30 + '\n' ) 

    objTable.print_table()

    # BFS Goaldriven
    table = goal_driven_dfs(tree=obj.tree, start_node=obj.start_node, goal_node=obj.goal_node)
    objTable = PrintGraphTable(table)
    print('\n' +"--"*30 + "Goal driven"+ "--"*30 + '\n' ) 

    objTable.print_table()



def main ():
    isTreeEntered = False
    isTreeWithHeuristics = False
    # Enter Tree Only                     :\t 0
    print('''
    BFS Data driven and goal            :\t 1
    DFS Data driven and goal            :\t 2
    BFS And DFS Data driven and goal    :\t 3
    Hill-Climbing Data driven and goal  :\t 4
''')
#     tree = {
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
    option = int(input("Select option : "))
    match option:
        case 0:
            
            isValue = input("Tree Is Heuristic Value: yes or no")
            if (isValue.lower() == "no"):
                isTreeEntered = True
                isTreeWithHeuristics = True
                user_tree = take_input_graph()
                start_node = input("Enter Start node : ")
                goal_node = input("Enter Goal node : ")
                obj = TreeClass(tree=user_tree, start_node=start_node, goal_node=goal_node)

            else:
                user_tree = take_input_graph(isHillClimbing=True)
                start_node = input("Enter Start node : ")
                goal_node = input("Enter Goal node : ")
                obj = TreeClass(tree=user_tree, start_node=start_node, goal_node=goal_node)
                isTreeEntered = True
                isTreeWithHeuristics = False

        case 1:
            if (isTreeEntered):
                return bfs_data_goal(obj = obj)
            user_tree = take_input_graph()
            start_node = input("Enter Start node : ")
            goal_node = input("Enter Goal node : ")
            isTreeWithHeuristics = False
            obj = TreeClass(tree=user_tree, start_node=start_node, goal_node=goal_node)
            bfs_data_goal(obj = obj)
        case 2:
            if (isTreeEntered):
                return bfs_data_goal(obj = obj)
            user_tree = take_input_graph()
            start_node = input("Enter Start node : ")
            goal_node = input("Enter Goal node : ")
            isTreeWithHeuristics = False
            obj = TreeClass(tree=user_tree, start_node=start_node, goal_node=goal_node)
            dfs_data_goal(obj = obj)
            
        case 3:
            if (isTreeEntered):
                bfs_data_goal(obj = obj)
                dfs_data_goal(obj = obj)
                return
            
            user_tree = take_input_graph()
            start_node = input("Enter Start node : ")
            goal_node = input("Enter Goal node : ")
            isTreeWithHeuristics = False
            obj = TreeClass(tree=user_tree, start_node=start_node, goal_node=goal_node)
            bfs_data_goal(obj = obj)
            dfs_data_goal(obj = obj)
            
        case 4:
            # if (isTreeEntered and not isTreeWithHeuristics): return print("Please Enter Tree with Heuristics value")
            # if (isTreeEntered and isTreeWithHeuristics):
            #     return hill(obj = obj)
            
            # tree = {
            #     "A": ["B", "C", "D"],
            #     "B": ["E", "F"],
            #     "C": ["E", "G"],
            #     "D": ["E", "F", "G"],
            #     "E": ["H", "I"],
            #     "F": ["I"],
            #     "G": ["H", "I"],
            #     "H": [],
            #     "I": [],
            #     "J": [],
            # }

            # # Heuristic values for each node
            # heuristics = {
            #     "A": 10,
            #     "B": 9,
            #     "C": 5,
            #     "D": 8,
            #     "E": 4,
            #     "F": 2,
            #     "G": 6,
            #     "H": 2,
            #     "I": 8,
            #     "J": 0  # Assuming J is not connected and has a heuristic value
            # }


            user_tree = take_input_graph(isHillClimbing=True)
            start_node = input("Enter Start node : ")
            goal_node = input("Enter Goal node : ")
            # start_node = "A"
            # goal_node = "H"
            obj = TreeClass(tree=user_tree, start_node=start_node, goal_node=goal_node)
            # obj = TreeClass(tree=[tree, heuristics], start_node=start_node, goal_node=goal_node)
            hill(obj = obj)

            
main()