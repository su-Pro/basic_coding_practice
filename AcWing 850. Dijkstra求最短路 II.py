import heapq
N, M, D = int(1.5e5 + 5), int(1.5e5 + 5), float('inf')
h, e, ne, edges, idx = [0] * N, [0] * M, [0] * M, [0] * M, 0
dist, vt = [D] * N, [False] * N
def ipt_helper(): return map(int, input().split())


n, m = ipt_helper()


def add(u, v, z):
    global idx
    idx += 1
    e[idx] = v
    ne[idx] = h[u]
    h[u] = idx
    edges[idx] = z


def heapfly_dijkstra():
    pq = []
    dist[1] = 0
    heapq.heappush(pq, (0, 1))
    while pq:
        d, u_idx = heapq.heappop(pq)
        if vt[u_idx]:
            continue
        vt[u_idx] = True
        # 遍历所有边，找到下一个最小的
        u = h[u_idx]
        while u:
            v = e[u]
            # 考虑是否加入到heap中，并更新dist
            if dist[v] > d + edges[u]:
                dist[v] = d + edges[u]
                heapq.heappush(pq, (dist[v], v))
            u = ne[u]
    return dist[n]


for _ in range(m):
    u, v, z = ipt_helper()
    add(u, v, z)

dist_n = heapfly_dijkstra()

print(
    -1 if dist_n == D else dist_n
)
