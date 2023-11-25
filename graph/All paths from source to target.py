"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 
0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a 
directed edge from node i to node graph[i][j]).
"""


class Solution:
    def __init__(self):
        self.result = []
        self.path = [0]

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        if not graph:
            return []
        self.dfs(graph, 0)
        return self.result

    def dfs(self, graph, root: int):
        if root == len(graph) - 1:
            self.result.append(self.path[:])
            return

        for node in graph[root]:
            self.path.append(node)
            self.dfs(graph, node)
            self.path.pop()
            
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [4],
    4: [],
    5: []
}

sol = Solution()
result = sol.allPathsSourceTarget(graph)
print(result)