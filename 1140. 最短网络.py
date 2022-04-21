N = 105
edges, p = [], [0] * N

n = int(input())
g = [list(map(int, input().split())) for x in range(n)]


def find(x):
    if x != p[x]:
        x = find(p[x])
    return p[x]


def kruskal():
    added_edge_cnt = path_sum = 0
    for i in range(1, n + 1):
        p[i] = i
    edges.sort(key=lambda edge: edge[2])

    # build
    for u, v, z in edges:
        u, v = find(u), find(v)
        if u != v:
            p[u] = v
            added_edge_cnt += 1
            path_sum += z

    return path_sum


for x in range(n):
    for y in range(n):
        if g[x][y]:
            edges.append((x, y, g[x][y]))

print(
    kruskal()
)
