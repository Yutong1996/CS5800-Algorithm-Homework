from heapq import heappush, heappop
from collections import defaultdict, deque

# Dijkstra's algorithm for finding shortest path distances
def dijkstra(graph, source):
    # Initialize all distances to infinity
    dist = {v: float('inf') for v in graph}
    # Distance to the source from itself is zero
    dist[source] = 0
    # Priority queue for maintaining vertices to be explored
    queue = [(0, source)]
    while queue:
        # Extract the vertex with the minimum distance
        distance, u = heappop(queue)
        # Loop through the neighbors of the current vertex
        for v, w in graph[u]:
            # Calculate new distance for the current path
            new_dist = distance + w
            # If the new calculated distance is less, update it
            if new_dist < dist[v]:
                dist[v] = new_dist
                # Add the updated distance to the priority queue
                heappush(queue, (new_dist, v))
    # Return the shortest distances from source to all vertices
    return dist

# Function to count shortest paths from source to target
def count_shortest_paths(graph, source, target):
    # Get shortest path distances using Dijkstra's algorithm
    shortest_distances = dijkstra(graph, source)
    
    # Create a new graph containing only edges on shortest paths
    dag = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            # Include edge if it's on a shortest path
            if shortest_distances[u] + w == shortest_distances[v]:
                dag[u].append(v)
    
    # Initialize counts of shortest paths with zero
    count = {v: 0 for v in graph}
    # There's one shortest path from the source to itself
    count[source] = 1
    # Queue for vertices sorted in topological order
    topo_sort = deque([source])
    while topo_sort:
        # Get the next vertex in topological order
        u = topo_sort.popleft()
        for v in dag[u]:
            # Add the count of shortest paths to u to the count for v
            count[v] += count[u]
            # Add v to the queue to continue the topological order
            topo_sort.append(v)
    
    # The count for the target vertex is the number of shortest paths
    return count[target]

# Example graph defined as an adjacency list with edge weights
graph = {
    's': [('a', 2), ('b', 1)],
    'a': [('b', 1), ('c', 2), ('t', 4)],
    'b': [('c', 2), ('t', 3)],
    'c': [('t', 1)],
    't': []
}

# Source and target vertices
source = 's'
target = 't'

print(count_shortest_paths(graph, source, target))  # Output should be 2

graph1 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5), ('E', 1)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 2)],
    'E': [('B', 1), ('D', 2)]
}

source = 'A'
target = 'D'
print(count_shortest_paths(graph1, source, target))  # Output should be 2