def find(u):
    if dsu[u] != u:
        dsu[u] = find(dsu[u])
    return dsu[u]


N, n = 305, int(input())
# 1. 将发电站建立成虚拟源点
edges, dsu = [(n + 1, v, int(input())) for v in range(1, n + 1)], [0] * N

# 2. 读边，裸kruskal
graphs = [list(map(int, input().split())) for x in range(n)]

for u in range(n):
    for v in range(n):
        edges.append((u + 1, v + 1, graphs[u][v]))


for u in range(1, n + 1):
    dsu[u] = u

edges.sort(key=lambda edge: edge[2])

ans = 0
for u, v, w in edges:
    u, v = find(u), find(v)
    if u != v:
        dsu[u], ans = v, ans + w

print(ans)
