import collections
N, M, D = 800 + 5, 1450 + 5, float('inf')
h, e, ne, w, idx = [0] * N, [0] * M, [0] * M, [0] * M, 0
def ipt(): return map(int, input().split())


c, n, m = ipt()
cow_to_n = []


def add(u, v, z):
    global idx
    idx += 1
    e[idx] = v
    ne[idx] = h[u]
    h[u] = idx
    w[idx] = z


def spfa(st):
    dist, vt = [D] * N, [False] * N
    que = collections.deque([st])
    dist[st] = 0
    vt[st] = True

    while que:
        u_idx = que.popleft()
        u = h[u_idx]
        vt[u_idx] = False
        while u:
            v = e[u]
            if dist[v] > dist[u_idx] + w[u]:
                dist[v] = dist[u_idx] + w[u]
                if not vt[v]:
                    que.append(v)
                    vt[v] = True
            u = ne[u]

    path_sum = 0

    for cow_no in cow_to_n:
        if dist[cow_no] == D:
            return D
        path_sum += dist[cow_no]

    return path_sum
    # 路径求和


for _ in range(c):
    cow_to_n.append(int(input()))

for _ in range(m):
    u, v, z = ipt()
    add(u, v, z)
    add(v, u, z)

res = D
for st in range(1, n + 1):
    path_sum = spfa(st)
    res = min(res, path_sum)

print(res)
