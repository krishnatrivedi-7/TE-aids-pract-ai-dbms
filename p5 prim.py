n = int(input("Enter number of vertices: "))
print("Enter the adjacency matrix (use 0 for no edge):")
g = [list(map(int, input().split())) for _ in range(n)]

selected = [0]*n
selected[0] = 1
edges, cost = 0, 0

while edges < n-1:
    m = 99999
    x = y = 0
    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and g[i][j]:
                    if m > g[i][j]:
                        m = g[i][j]
                        x, y = i, j
    print(f"Edge {x}-{y} cost: {g[x][y]}")
    cost += g[x][y]
    selected[y] = 1
    edges += 1

print("Total cost of MST:", cost)


# Enter number of vertices: 4
# Enter the adjacency matrix (use 0 for no edge):
# 0 2 0 6
# 2 0 3 8
# 0 3 0 0
# 6 8 0 0
