N, M = 105, 50000  # 用于方便的建图，顶点个数
def ipt(): return map(int, input().split())


def table_build():
    gh, vt = [[0] * N] * N, [False] * N

    def dfs(u):
        # 正序遍历图
        print(u)
        vt[u] = True
        # 遍历所有的连边
        for v in range(1, n + 1):
            if gh[u][v] and not vt[v]:
                dfs(v)

        # 逆序遍历图
        print(u)

    n, m = ipt()
    for _ in range(m):
        u, v = ipt()
        gh[u][v] = 1  # u -> v 单向有向边
        # gh[u][v] = gh[v][u] = 1 # u -> v; v -> u 双向边
    dfs(1)


# def link_start_build():
h, to_e, prev_ne, idx = [0] * N, [0] * M, [0] * M, 0  # 单向图
vt = [False] * N
# h,to_e,prev_ne,idx = [0] * N,[0] * M * 2,[0] * M * 2,0  # 无向图


def add(u, v):
    global idx
    idx += 1
    to_e[idx] = v
    prev_ne[idx] = h[u]
    h[u] = idx


def dfs(u):
    print(u)
    vt[u] = True
    u = h[u]
    while u:
        v = to_e[u]
        u = prev_ne[u] #一定记得修改u 在 dfs下一个节点前!!!!!!
        if vt[v]:
            continue
        dfs(v)


n, m = ipt()
for _ in range(m):
    u, v = ipt()
    add(u, v)
    # add(v,u) 无相图

dfs(1)

# table_build()
# link_start_build()

# test_data
# 4 5
# 1 2
# 2 3
# 3 4
# 1 3
# 1 4
