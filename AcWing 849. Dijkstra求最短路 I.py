def ipt_helper(): return map(int, input().split())


N, M, d_max = 510, int(1e5 + 10), float('inf')
dist, g_edges, vt = [d_max] * N, [[d_max] * N for x in range(N)], [False] * N
n, m = ipt_helper()


def dijkstra():
    dist[1] = 0
    for _ in range(n):
        u = 0
        for _u in range(1, n + 1):
            if not vt[_u] and (u == 0 or dist[u] > dist[_u]):
                u = _u
        for v in range(1, n + 1):
            dist[v] = min(dist[v], dist[u] + g_edges[u][v])
        vt[u] = True
    return dist[n]


for _ in range(m):
    u, v, z = ipt_helper()
    g_edges[u][v] = min(g_edges[u][v], z)

dist_n = dijkstra()

print(-1 if dist_n == d_max else dist_n)
