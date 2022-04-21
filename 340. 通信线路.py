import collections

N, M = 2010, 20010

h, e, ne, w, idx = [0] * N, [0] * M, [0] * M, [0] * M, 0


def add(u, v, z):
    global idx
    idx += 1
    e[idx] = v
    ne[idx] = h[u]
    h[u] = idx
    w[idx] = z


def check(target_w):
    dist, vt, que = [float('inf')] * N, [False] * N, collections.deque()
    que.append(1)
    dist[1] = 0

    while que:
        u_idx = que.popleft()
        if vt[u_idx]: continue
        vt[u_idx] = True

        u = h[u_idx]
        while u:
            v, can_go = e[u], w[u] > target_w
            if dist[v] > dist[u_idx] + can_go:
                dist[v] = dist[u_idx] + can_go
                if can_go:
                    que.append(v)
                else:
                    que.appendleft(v)
            u = ne[u]
    return dist[n] <= k



def ipt():
    return map(int, input().split())


n, m, k = ipt()
for _ in range(m):
    u, v, z = ipt()
    add(u, v, z)
    add(v, u, z)

l, r = 0, int(1e6 + 1)
while l < r:
    m = l + r >> 1
    if check(m):
        r = m
    else:
        l = m + 1
if r == 1e6 + 1:
    print(-1)
else:
    print(r)
