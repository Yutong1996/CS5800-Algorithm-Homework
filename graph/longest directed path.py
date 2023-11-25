'''
Given adjacency list access to a
directed acyclic graph, present an algorithm that finds the longest directed path in the graph.
A directed path is a sequence of distinct vertices u1, u2, . . . , ul such that for 1 ≤ i ≤ l - 1
there as an edge from ui to ui+1. (Hint: use the topological order).
'''


from collections import deque

class DAG:
    def __init__(self, graph):
        self.graph = graph

    def topological_sort(self):
        # Initialize the in-deree dictionary, setting initial in-degrees of all nodes to 0
        in_degree = {node: 0 for node in self.graph}

        # Calculate the in-degrees of each node based on the provided graph
        for node in self.graph:
            for neighbor in self.graph[node]:
                in_degree[neighbor] += 1
                # print(neighbor, in_degree)

        # Initialize a queue and enqueue nodes with in-degree 0
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        top_order = [] # Store the result of topological sorting

        # Topological sorting main loop
        while queue:
            node = queue.popleft() # Dequeue a node
            top_order.append(node) # Append the node to the topological sort

            # Upate the in-degree of neighboring nodes
            for neighbor in self.graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    # If in-degree becoms 0, add this node into queue
                    queue.append(neighbor) 

        return top_order

    def find_longest_path(self):
        # Get the result of topological sorting
        top_order = self.topological_sort()
        print(top_order)
        # initialize the dict to store the longest paths
        longest_path = {node: [] for node in self.graph}

        # iterate through the sorted result
        for node in top_order:
            # iterate through thr neighboring nodes of the current node
            for neighbor in self.graph[node]:
                # if the path length of the neighbor is less than the current node's 
                # path plus 1, update thr path of neighbor to the longer one
                if len(longest_path[neighbor]) < len(longest_path[node]) + 1:
                    longest_path[neighbor] = longest_path[node] + [node]

        # find the node in the dictionary with the longest path and return that 
        # node along with its longest path
        result = max(longest_path, key=lambda k: len(longest_path[k]))
        return longest_path[result] + [result]


# Example graph represented as an adjacency list
graph1 = {
    1: [2],
    0: [2, 1],
    3: [4],
    2: [3],
    4: []
}
g1 = DAG(graph1)
longest_path = g1.find_longest_path()
print("Longest Path:", longest_path)

graph2 = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
}
g2 = DAG(graph2)
longest_path = g2.find_longest_path()
print("Longest Path:", longest_path)

graph3 = {
    0: [1, 2], 
    1: [3, 4], 
    2: [5], 
    3: [], 
    4: [5], 
    5: [6], 
    6: [7], 
    7: []
}
g3 = DAG(graph3)
longest_path = g3.find_longest_path()
print("Longest Path:", longest_path)

graph4 = {
    5: [7, 8], 
    0: [1, 2, 3], 
    1: [4], 
    2: [4, 5], 
    3: [5], 
    4: [6, 7], 
    7: [9, 10], 
    6: [9], 
    8: [10], 
    10: [11], 
    9: [11], 
    11: []
}
g4 = DAG(graph4)
longest_path = g4.find_longest_path()
print("Longest Path:", longest_path)

graph5 = {
    0: [1, 2, 3],
    1: [4, 5], 
    2: [5, 6], 
    3: [6, 7], 
    4: [8], 
    5: [8, 9], 
    6: [9, 10], 
    7: [10], 
    8: [11], 
    9: [11], 
    10: [11], 
    11: []
}
g5 = DAG(graph5)
longest_path = g5.find_longest_path()
print("Longest Path:", longest_path)

graph6 = {
    0: [1, 3],
    1: [2, 3],
    2: [3],
    3: []
}
g6 = DAG(graph6)
longest_path = g6.find_longest_path()
print("Longest Path:", longest_path)

