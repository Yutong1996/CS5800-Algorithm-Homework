'''
In an undirected graph, a cycle is defined as a sequence
of unique vertices u1, u2, . . . , ul such that each vertex has an edge to the next, i.e. there is
an edge between ui and ui+1 for 1 ≤ i ≤ l - 1, and an edge between u1 and ul. Given an
undirected graph G with adjacency list access:
1. (5 Points) Provide an algorithm based on depth-first search that either finds a cycle
or reports that there are no cycles in the graph. (Doing the next part would give you
full credit for this part.)
2. (20 points) A cycle is minimal if no strict subset of its vertices form a cycle. Provide
an algorithm based on depth-first search that finds a minimal cycle or reports that
there are no cycles in the graph.
Prove correctness and analyze the run time. The algorithms should run in O(n + m) time.
'''


# 1.
def has_cycle(graph):
    visited = set()

    def dfs(node, parent, path):
        path.append(node)
        # print('append')
        # print(path)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                cycle = dfs(neighbor, node, path)
                if cycle:
                    return cycle
            elif neighbor != parent and neighbor in path:
                # If neighbor is visited and not the node we visited just before thr current node, 
                # a cycle is detected
                index = path.index(neighbor)
                return path[index:]
        path.pop()
        # print('pop')
        # print(path)

        return False

    for start_node in graph:
        if start_node not in visited:
            cycle = dfs(start_node, None, [])
            if cycle:
                return cycle

    return False


graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E', 'F'],
    'D': ['B'],
    'E': ['B', 'C'],
    'F': ['G']
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

graph3 = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['B']
}

print("Graph 1 Cycle:", has_cycle(graph1))
print("Graph 2 Cycle:", has_cycle(graph2))
print("Graph 3 Cycle:", has_cycle(graph3))


# 2.
def find_minimal_cycle(graph):
    visited = set()
    min_size = float('inf')
    minimal_cycle = []
    
    def dfs(node, parent, path):
        nonlocal min_size, minimal_cycle

        path.append(node)
        # print('append')
        # print(path)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                cycle = dfs(neighbor, node, path)
                if cycle and len(cycle) < min_size:
                    min_size = len(cycle)
                    minimal_cycle = cycle
            elif neighbor != parent and neighbor in path:
                # If neighbor is visited and not the node we visited just before thr current node, 
                # a cycle is detected
                # print(neighbor)
                index = path.index(neighbor)
                cycle = path[index:]
                if len(cycle) < min_size:
                    min_size = len(cycle)
                    minimal_cycle = cycle

            
        path.pop()
        # print('pop')
        # print(path)

        return minimal_cycle

    for start_node in graph:
        if start_node not in visited:
            cycle = dfs(start_node, None, [])
            if cycle:
                return cycle

    return False

graph01 = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2, 6],
    5: [2, 3, 6],
    6: [5, 4]
}

minimal_cycle = find_minimal_cycle(graph01)
print(minimal_cycle) #[2, 4, 6, 5]

graph02 = {
    4: [5, 2],
    1: [2, 3],
    2: [3, 4],
    3: [1, 2, 5],
    5: [3, 4]
}

minimal_cycle = find_minimal_cycle(graph02)
print(minimal_cycle) #[3, 1, 2]

graph4 = {
    6: [9], 
    7: [9, 10], 
    8: [10], 
    10: [7, 8, 11], 
    9: [6, 7, 11], 
    11: [9, 10],
    5: [2, 3], 
    0: [1, 12, 2, 3], 
    1: [0, 12, 4], 
    2: [0, 4, 5], 
    3: [0, 5], 
    4: [1, 2], 
    12: [0, 1]
}
minimal_cycle = find_minimal_cycle(graph4)
print(minimal_cycle) #[2, 0, 1, 4]