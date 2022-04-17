import collections

helper_ipt = lambda: map(int, input().split())

N = int(1e5 + 10)
n, m = helper_ipt()
h, to_e, prev_ne, idx = [0] * N, [0] * N, [0] * N, 0


def add(u, v):
    global idx
    idx += 1
    to_e[idx] = v  # 1. 存出边
    prev_ne[idx] = h[u]  # 2. 修改指针，准备加新边
    h[u] = idx  # 3. 加新边


for _ in range(m):
    u, v = helper_ipt()
    add(u, v)


def bfs():
    d, que = [-1] * N, collections.deque()
    d[1] = 0
    que.append(1)
    while que:
        u_idx = que.popleft()
        u = h[u_idx]
        while u:
            v = to_e[u]
            u = prev_ne[u]
            # 加入待搜索的队列中
            if d[v] == -1:
                que.append(v)
                # 更新d的距离
                d[v] = d[u_idx] + 1
    return d[n]

minimum_step = bfs()

print(
    minimum_step
)
