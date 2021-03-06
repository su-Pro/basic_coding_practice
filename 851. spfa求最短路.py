import collections
def ipt_helper(): return map(int, input().split())


N, M, D = int(1e5 + 5), int(1e5 + 5), float('inf')
dist, vt = [D] * N, [False] * N

h, e, ne, edges, idx = [0] * N, [0] * M * 2, [0] * M * 2, [0] * M * 2, 0

n, m = ipt_helper()


def add(u, v, z):
    global idx
    idx += 1
    e[idx] = v
    ne[idx] = h[u]
    h[u] = idx
    edges[idx] = z


def spfa():
    que = collections.deque([1])
    dist[1] = 0
    vt[1] = True

    while que:
        u_idx = que.popleft()
        u = h[u_idx]
        vt[u_idx] = False
        while u:
            v = e[u]
            if dist[v] > dist[u_idx] + edges[u]:
                dist[v] = dist[u_idx] + edges[u]
                if not vt[v]:
                    que.append(v)
                    vt[v] = True
            u = ne[u]

    return dist[n]


for _ in range(m):
    u, v, z = ipt_helper()
    add(u, v, z)

dist_n = spfa()
print('impossible' if dist_n == D else dist_n)
