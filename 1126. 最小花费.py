N = 2010
def ipt(): return map(int, input().split())


edge, dist, vt = [[0] * N for x in range(N)], [0] * N, [False] * N
n, m = ipt()


def dijkstra():
    dist[st] = 1

    for _ in range(n):
        u = 0
        for _u in range(1, n + 1):
            # TODO: 为什么这里是找更大的呢边呢？
            if not vt[_u] and (u == 0 or dist[u] < dist[_u]):
                u = _u
        vt[u] = True
        for v in range(1, n + 1):
            dist[v] = max(dist[v], dist[u] * edge[u][v])


for _ in range(m):
    u, v, z = ipt()
    edge[u][v] = edge[v][u] = max(edge[u][v], (100.0 - z) / 100)

st, ed = ipt()
dijkstra()
print("%.8f" % (100 / dist[ed]))
