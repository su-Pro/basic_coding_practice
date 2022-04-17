import collections

N = int(1e5 + 10)
h, e, ne, idx, in_deg = [0] * N, [0] * N, [0] * N, 0, [0] * N
helper_ipt = lambda: map(int, input().split())


def add(u, v):
    global idx
    idx += 1
    e[idx] = v
    ne[idx] = h[u]
    h[u] = idx


n, m = helper_ipt()
for _ in range(m):
    u, v = helper_ipt()
    add(u, v)
    in_deg[v] += 1


def bfs():
    que, top_sequence = collections.deque(), []
    # 这里由于初始化in_deg长度是N，可以遍历所有图中的节点，来确保正确的初始化0入度点
    for i in range(1, n + 1):
        if in_deg[i] == 0: que.append(i)
    while que:
        u_idx = que.popleft()
        u = h[u_idx]
        top_sequence.append(u_idx)
        while u:
            v = e[u]
            u = ne[u]
            in_deg[v] -= 1
            if in_deg[v] == 0: que.append(v)
    return top_sequence


A = bfs()

if len(A) == n:
    print(*A)
else:
    print(-1)
