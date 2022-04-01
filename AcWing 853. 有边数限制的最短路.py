N, M = 500 + 10, 10000 + 10
n, m, k = map(int, input().split())
edges, d, last = [], [float('inf')] * N, [float('inf')] * N


def bellman_ford():
    d[1] = 0
    for _ in range(k):
        last = d.copy()
        for i in range(m):
            x, y, w = edges[i]
            d[y] = min(d[y], last[x] + w)


for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

bellman_ford()
print(
    'impossible' if d[n] == float('inf') else d[n]
)
