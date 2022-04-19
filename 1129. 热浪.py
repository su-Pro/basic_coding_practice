import collections
def ipt_helper(): return map(int, input().split())


N, M, D = int(1e5 + 5), int(1e5 + 5), float('inf')
dist, vt = [D] * N, [False] * N

h, e, ne, edges, idx = [0] * N, [0] * M, [0] * M, [0] * M, 0

n, m, st, ed = ipt_helper()


def add(u, v, z):
    global idx
    idx += 1
    e[idx] = v
    ne[idx] = h[u]
    h[u] = idx
    edges[idx] = z


def spfa():
    que = collections.deque([1])
    dist[st] = 0
    vt[st] = True

    while que:
        u_idx = que.popleft()
        vt[u_idx] = False
        u = h[u_idx]
        while u:
            v = e[u]
            if dist[v] > dist[u] + edges[u]:
                dist[v] = dist[u] + edges[u]
                if v in vt:
                    continue
                que.append(v)
                vt[v] = True
            u = ne[u]

    return dist[ed]


for _ in range(m):
    u, v, z = ipt_helper()
    add(u, v, z)

dist_n = spfa()
print(-1 if dist_n == D else dist_n)
