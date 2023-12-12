from heapq import heappush, heappop
from collections import defaultdict

def prim_mst(graph, start):
    visited = {v: False for v in graph}
    parent = {v: None for v in graph}
    cost = {v: float('inf') for v in graph}
    cost[start] = 0
    queue = [(0, start)]
    mst_edges = set()

    while queue:
        _, u = heappop(queue)
        if visited[u]:
            continue

        visited[u] = True
        if parent[u] is not None:
            mst_edges.add((parent[u], u, cost[u]))

        for v, weight in graph[u]:
            if not visited[v] and cost[v] > weight:
                cost[v] = weight
                parent[v] = u
                heappush(queue, (weight, v))

    return mst_edges

def has_unique_mst(graph):
    start_vertex = next(iter(graph))  # Arbitrary start vertex
    mst_edges = prim_mst(graph, start_vertex)

    # Check if there is an alternative edge for each edge in the MST
    for edge in mst_edges:
        u, v, weight = edge
        graph[u].remove((v, weight))
        graph[v].remove((u, weight))

        new_mst_edges = prim_mst(graph, start_vertex)

        # Add the edge back to the graph
        graph[u].append((v, weight))
        graph[v].append((u, weight))

        # Check if the new MST has the same weight as the original
        if sum(weight for _, _, weight in new_mst_edges) == sum(weight for _, _, weight in mst_edges):
            return False

    return True

# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5), ('E', 1)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 2)],
    'E': [('B', 1), ('D', 2)]
}

print(has_unique_mst(graph))  # Outputs whether the graph has a unique MST