def ipt(): return map(int, input().split())


N, M, D = 105, 210, float('inf')
graph_edges, vt, dist = [[D] * N for x in range(N)], [False] * N, [D] * N
n, m = ipt()


def dijkstra():
    dist[1] = 0
    for _ in range(n):
        x = 0
        # 1. 找到最小的点x
        for u in range(1, n + 1):
            if not vt[u] and (x == 0 or dist[x] > dist[u]):
                x = u
        # 2. 计算周边节点
        for v in range(1, n + 1):
            dist[v] = min(dist[v], dist[x] + graph_edges[x][v])
        vt[x] = True


for _ in range(m):
    u, v, z = ipt()
    graph_edges[u][v] = min(graph_edges[u][v], z)
    graph_edges[v][u] = min(graph_edges[u][v], z)

dijkstra()
# TODO: heapify_dijkstra + spfa
res = 0
for u in range(1, n + 1):
    if dist[u] == D:
        res = -1
        break
    res = max(dist[u], res)
print(res)
