N, M = 1010,10010
# 建正、反图
h, un_h, to_e, prev_ne, idx = [0] * N, [0] * N, [0] * M * 2, [0] * M * 2, 0
n, m = map(int, input().split())


def add(h, u, v):
    global idx
    idx += 1
    to_e[idx] = v
    prev_ne[idx] = h[u]
    h[u] = idx


for _ in range(m):
    u, v = map(int, input().split())
    add(h, u, v)
    add(un_h, v, u)  # 反向图要从v到u 注意关系

cnt = 0


def dfs(h, i, vs):
    vs[i] = True
    u = h[i]
    while u:
        v = to_e[u]
        if not vs[v]: dfs(h, v, vs)
        u = prev_ne[u]


for i in range(1, n + 1):
    # 统计每个节点从两个方向能到达的节点数量
    vs, un_vs = [False] * N, [False] * N
    dfs(h, i, vs)
    dfs(un_h, i, un_vs)
    can_arrive = [x for x in range(1, n + 1) if vs[x] or un_vs[x]]
    if len(can_arrive) == n: cnt += 1

print(cnt)
