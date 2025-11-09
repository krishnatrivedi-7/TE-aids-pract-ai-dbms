from collections import deque

# Function to build an undirected graph from user input
def create_graph():
    graph = {}
    n = int(input("Enter number of vertices: "))
    print("Enter vertex names (like A, B, C...):")
    vertices = [input().strip() for _ in range(n)]

    # Initialize adjacency list
    for v in vertices:
        graph[v] = []

    e = int(input("Enter number of edges: "))
    print("Enter each edge (example: A B means edge between A and B):")
    for _ in range(e):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)  # since graph is undirected

    return graph


# Recursive DFS function
def dfs_recursive(node, visited, graph):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs_recursive(neighbour, visited, graph)


# BFS function (uses queue)
def bfs(start, graph):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


# -------------------- MAIN PROGRAM --------------------
graph = create_graph()

start = input("Enter the starting node: ").strip()

print("\nDFS (Recursive) traversal:")
dfs_recursive(start, set(), graph)

print("\nBFS traversal:")
bfs(start, graph)


# Enter number of vertices: 4
# Enter vertex names (like A, B, C...):
# A
# B
# C
# D
# Enter number of edges: 4
# Enter each edge (example: A B means edge between A and B):
# A B
# A C
# B D
# C D
# Enter starting node: A
