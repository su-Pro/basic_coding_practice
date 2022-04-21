N, M = 505, int(1e5 + 5)  # 边 >> 点 : 稠密图
D = float('inf')
dist, vt, prev, g = [D] * N, [False] * N, [-1] * N, [[D] * N for x in range(N)]


def ipt(): return map(int, input().split())


def prim():
    dist[1] = 0
    total_path_sum = 0
    for _ in range(n):
        u = 0
        for _u in range(1, n + 1):
            if not vt[_u] and (u == 0 or dist[_u] < dist[u]):
                u = _u
        vt[u] = True
        total_path_sum += dist[u]

        # 更新所有出边
        for v in range(1, n + 1):
            if dist[v] > g[u][v] and not vt[v]:
                dist[v] = g[u][v]
                prev[v] = u
    return total_path_sum


n, m = ipt()
for _ in range(m):
    u, v, z = ipt()
    g[u][v] = g[v][u] = min(g[u][v], z)

path_sum = prim()
print(
    'impossible' if path_sum == D else path_sum
)
