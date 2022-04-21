import heapq

helper_ipt = lambda: map(int, input().split())
N, M, D = int(5e5 + 5), int(1e5 + 5), float('inf')

n, m = helper_ipt()
source = [1] + list(helper_ipt())
dists = [[D] * N for x in range(6)]
# 用堆dijkstra 做
h, e, ne, w, idx = [0] * N, [0] * M * 2, [0] * M * 2, [0] * M * 2, 0


def add(u, v, z):
    global idx
    idx += 1
    e[idx] = v
    ne[idx] = h[u]
    h[u] = idx
    w[idx] = z


for _ in range(m):
    u, v, z = helper_ipt()
    add(u, v, z)
    add(v, u, z)


def heapify_dijkstra(st, dist):
    pq, vt = [], [False] * N
    dist[st] = 0
    heapq.heappush(pq, (0, st))
    while pq:
        d, u_idx = heapq.heappop(pq)
        if vt[u_idx]: continue
        vt[u_idx] = True
        u = h[u_idx]
        while u:
            v = e[u]
            if dist[v] > d + w[u]:
                dist[v] = d + w[u]
                heapq.heappush(pq, (dist[v], v))
            u = ne[u]


for idx, st in enumerate(source):
    heapify_dijkstra(st, dists[idx])


def dfs(level, start, path_sum):
    #  TODO base case 再考虑一下？

    if level > 5: return path_sum
    res = float('inf')
    # 考虑每个位置的可能性
    for i in range(1, 6):
        if not vt[i]:
            vt[i] = True
            res = min(res, dfs(level + 1, i, dists[start][source[i]] + path_sum))
            vt[i] = False
    return res


vt = [False] * 6
print(dfs(1, 0, 0))
