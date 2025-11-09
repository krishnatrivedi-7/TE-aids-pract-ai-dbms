def a_star(graph, start, goal, h):
    open_set = {start}
    came = {}
    g = {n: float('inf') for n in graph}
    f = {n: float('inf') for n in graph}
    g[start] = 0
    f[start] = h[start]

    while open_set:
        n = min(open_set, key=lambda x: f[x])      # pick node with smallest f-score
        if n == goal:
            path = [n]
            while n in came:
                n = came[n]
                path.append(n)
            return path[::-1]
        open_set.remove(n)
        for nb, cost in graph[n].items():
            t = g[n] + cost
            if t < g[nb]:
                came[nb] = n
                g[nb] = t
                f[nb] = t + h[nb]
                open_set.add(nb)

# ---------- USER INPUT PART ----------
n = int(input("Enter number of nodes: "))
graph = {}
for _ in range(n):
    node = input("Enter node name: ")
    edges = input(f"Enter neighbors and costs for {node} (e.g. B:2 C:4): ").split()
    graph[node] = {e.split(':')[0]: int(e.split(':')[1]) for e in edges}

h = {}
print("Enter heuristic values (node value):")
for node in graph:
    h[node] = int(input(f"{node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

print("Shortest Path:", a_star(graph, start, goal, h))
  
# for output
#   #Enter number of nodes: 6
# Enter node name: A
# Enter neighbors and costs for A (e.g. B:2 C:4): B:1 C:3
# Enter node name: B
# Enter neighbors and costs for B (e.g. B:2 C:4): A:1 D:3 E:1
# Enter node name: C
# Enter neighbors and costs for C (e.g. B:2 C:4): A:3 F:5
# Enter node name: D
# Enter neighbors and costs for D (e.g. B:2 C:4): B:3
# Enter node name: E
# Enter neighbors and costs for E (e.g. B:2 C:4): B:1 F:2
# Enter node name: F
# Enter neighbors and costs for F (e.g. B:2 C:4): C:5 E:2
# Enter heuristic values (node value):
# A: 7
# B: 6
# C: 2
# D: 5
# E: 1
# F: 0
# Enter start node: A
# Enter goal node: F
