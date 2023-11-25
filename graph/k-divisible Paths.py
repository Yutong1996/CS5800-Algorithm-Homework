'''
Given adjacency list access to a directed
graph G, two vertices s and t, and an integer k ≥ 1, give an algorithm that finds a path
from s to t such that the number of edges in the path is divisible by k, or concludes that no
such path exists. Prove correctness and analyze the run time. The algorithm should run in
O(k(n + m)) time.
'''


def find_k_divisible_path(graph, s, t, k):
  visited = set()
  current_path = []

  def dfs(node, edge_count):
    nonlocal current_path

    visited.add(node)
    current_path.append(node)

    if node == t and edge_count % k == 0:
      return current_path
  
    for neighbor in graph[node]:
      if neighbor not in visited or neighbor == t:
        # print(neighbor)
        edge_count += 1
        # recursively call DFS with an updated edge count
        result_path = dfs(neighbor, edge_count)
        # print(result_path)
        if result_path:
          return result_path # return the path if found
        # if no k-divisible path is found, backtrack by removing the current node 
        # from the path
        current_path.pop()
        edge_count -= 1

    return None
  
  # start dfs from the source node with an initial edge count of 0
  result_path = dfs(s, 0)

  return result_path if result_path else None

graph1 = {
  'A': ['B', 'C', 'E'],
  'B': [],
  'C': ['D'],
  'D': ['F'],
  'E': ['F'],
  'F': []
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E', 'F'],
    'E': ['G'],
    'F': ['G', 'H'],
    'G': ['H'],
    'H': []
}

result_path = find_k_divisible_path(graph2, 'A', 'H', 2)
print(result_path)

result_path = find_k_divisible_path(graph1, 'A', 'F', 2)
print(result_path)