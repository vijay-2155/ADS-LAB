# Program to perform BFT and DFT on a graph
# using Adjacency Matrix and Adjacency List

from collections import deque

# -------- Representation (a) Adjacency Matrix --------
graph_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

def bfs_matrix(start):
    visited = [False] * len(graph_matrix)
    queue = deque([start])
    visited[start] = True
    print("BFT (Adjacency Matrix):", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for i in range(len(graph_matrix)):
            if graph_matrix[node][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
    print()

def dfs_matrix(start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in range(len(graph_matrix)):
        if graph_matrix[start][i] == 1 and not visited[i]:
            dfs_matrix(i, visited)

print("Using Adjacency Matrix:")
bfs_matrix(0)
print("DFT (Adjacency Matrix):", end=" ")
dfs_matrix(0, [False]*len(graph_matrix))
print("\n")


# -------- Representation (b) Adjacency List --------
graph_list = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

def bfs_list(start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    print("BFT (Adjacency List):", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    print()

def dfs_list(start, visited=set()):
    print(start, end=" ")
    visited.add(start)
    for neighbor in graph_list[start]:
        if neighbor not in visited:
            dfs_list(neighbor, visited)

print("Using Adjacency List:")
bfs_list(0)
print("DFT (Adjacency List):", end=" ")
dfs_list(0, set())
print()
