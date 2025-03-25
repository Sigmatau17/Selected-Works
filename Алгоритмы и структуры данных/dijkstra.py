from sys import stdin
import numpy as np

def dijkstra_with_path(graph, start):
    n = len(graph)
    visited = [False] * n
    distance = [float('inf')] * n
    distance[start] = 0
    prev = [-1] * n

    for _ in range(n):
        min_dist = float('inf')
        min_index = -1

        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_index = i

        visited[min_index] = True

        for i in range(n):
            if not visited[i] and graph[min_index][i] != 0:
                new_dist = distance[min_index] + graph[min_index][i]
                if new_dist < distance[i]:
                    distance[i] = new_dist
                    prev[i] = min_index

    return distance, prev

def get_path(prev, end):
    if prev[end] == -1:
        return -1
    path = []
    current = end
    while current != -1:
        path.insert(0, current)
        current = prev[current]
    return path

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
n_m = list(map(int, str(lines[0]).split()))
n, m = n_m[0], n_m[1]

lines.pop(0)
weight_matrix = np.zeros((n, n))
for i in range(len(lines)):
    array = list(map(int, str(lines[i]).split()))
    weight_matrix[array[0]-1][array[1]-1] = array[2]
    weight_matrix[array[1]-1][array[0]-1] = array[2]

start_node = 1
end_node = len(weight_matrix)
shortest_distances, prev_nodes = dijkstra_with_path(weight_matrix, start_node - 1)
shortest_path = get_path(prev_nodes, end_node - 1)

if shortest_path == -1:
    print(-1)
else:
    print(' '.join(str(node + 1) for node in shortest_path))