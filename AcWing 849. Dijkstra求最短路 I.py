N = 510
n, m = map(int, input().split())
g, d, vs = [[float('inf')] * N for i in range(N)], [float('inf')] * N, [0] * N


def dijkstra():
    d[1] = 0
    for _ in range(n):
        x = 0
        for j in range(1, n + 1):
            if (not vs[j] and (x == 0 or d[x] > d[j])):
                x = j
        for y in range(1, n + 1):
            d[y] = min(d[y], d[x] + g[x][y])
        vs[x] = True

    if d[n] == float('inf'):
        return -1
    return d[n]


for _ in range(m):
    u, v, w = map(int, input().split())
    g[u][v] = min(g[u][v], w)

print(dijkstra())
