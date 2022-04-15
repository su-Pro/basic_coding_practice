import collections

N = int(1e5 + 10)
ipt = lambda: map(int, input().split())

n, m = ipt()
h, to_e, prev_ne, idx = [0] * N, [0] * N, [0] * N, 0
deg, top_a = [0] * (n + 1), []


def add(u, v):
    global idx
    idx += 1
    to_e[idx] = v
    prev_ne[idx] = h[u]
    h[u] = idx

for _ in range(m):
    u, v = ipt()
    add(u, v)
    deg[v] += 1

def bfs():
    que = collections.deque()
    # 1. 入度为0的点入度
    for i in range(1, n + 1):
        if deg[i] != 0: continue
        que.append(i)
    while que:
        u_idx = que.popleft()
        top_a.append(u_idx)
        u = h[u_idx]
        while u:
            v = to_e[u]
            deg[v] -= 1
            if deg[v] == 0:
                que.append(v)
            u = prev_ne[u]


bfs()

# 拓扑序的正确性在BFS的基础上，只要保证数量关系相等即可。
if len(top_a) == n:
    print(*top_a)
else:
    print(-1)
