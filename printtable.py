import pandas as pd
from tabulate import tabulate
class PrintGraphTable:
    def __init__(self, data, isHeuristics=False):
        self.data = data
        self.isHeuristics = isHeuristics
        
    def print_table(self):
        # print("YES rEACHED")
        # Print the results

        # for i, entry in enumerate(data):
        #     print(f"Step {i}: Open nodes = {entry.open_node}, Closed nodes = {entry.closed_node}")


        # Extract values to create a DataFrame, including the iteration number


        if (self.isHeuristics):
            print("yes please")
            data = {
            "Iteration": [i for i in range(len(self.data))],
            "Open Node": [(node.open_node) for node in self.data],
            "Closed Node": [(node.closed_node) for node in self.data]
            }
        else:
            data = {
                "Iteration": [i for i in range(len(self.data))],
                "Open Node": [' '.join(node.open_node) for node in self.data],
                "Closed Node": [' '.join(node.closed_node) for node in self.data]
            }


        # Create DataFrame
        df = pd.DataFrame(data, columns=["Iteration", "Open Node", "Closed Node"])

        # Print the DataFrame with tabulate for better console formatting
        print(tabulate(df, headers='keys', tablefmt='grid', stralign='left'))


        # Display the DataFrame
        # print(df.to_string(index=False))
