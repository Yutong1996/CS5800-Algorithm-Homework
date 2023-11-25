def longestPath(graph):
    def topologicalSort():
        def dfs(node):
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            topo_stack.append(node)

        topo_stack = []
        visited = [False] * len(graph)
        for v in range(len(graph)):
            if not visited[v]:
                dfs(v)
        return topo_stack[::-1]

    # Step 1: Perform a topological sort
    topo_order = topologicalSort()

    # Step 2: Initialize distances
    dist = [-float('inf')] * len(graph)
    dist[topo_order[0]] = 0
    predecessor = [-1] * len(graph) # for the track of the path

    # Step 3: Relaxation step
    for u in topo_order:
        for v in graph[u]:
            if dist[v] < dist[u] + 1:
                dist[v] = dist[u] + 1
                predecessor[v] = u

    # Step 4: Find the longest path
    max_length = max(dist)
    end_vertex = dist.index(max_length)
    
    # Step 5: Backtrack the path
    path = []
    while end_vertex != -1:
        path.append(end_vertex)
        end_vertex = predecessor[end_vertex]
    # if multiple paths exist, return one of them
    return path[::-1]

# Example graph represented as an adjacency list
graph1 = {
    1: [2],
    0: [2, 1],
    3: [4],
    2: [3],
    4: []
}

graph2 = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
}

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

graph6 = {
    0: [1, 3],
    1: [2, 3],
    2: [3],
    3: []
}

print(longestPath(graph1)) # 4
print(longestPath(graph2)) # 3
print(longestPath(graph3)) # 5
print(longestPath(graph4)) # 5
print(longestPath(graph5)) # 4
print(longestPath(graph6)) # 3
