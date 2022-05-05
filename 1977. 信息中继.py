import sys

sys.setrecursionlimit(10000000)  # 并查集的题，数据量在1e3时，一定记得放开加递归栈限制,否则会超时。


def bruteForce():
    n = int(input())
    g = [0] + [int(input()) for x in range(n)]

    cnt = 0
    for v in range(1, n + 1):
        vt, has_cycle, u = {v}, False, g[v]
        while u:
            if u in vt:
                has_cycle = True
                break
            vt.add(u)
            u = g[u]

        if not has_cycle:  # 当前节点没有的路径中没有环路
            cnt += 1

    print(cnt)


# TODO - DSU
def dsuCheckCycle():
    def find(u):
        if dsu[u] != u:
            dsu[u] = find(dsu[u])
        return dsu[u]

    N, n = int(1e3) + 5, int(input())
    dsu, graph = [0] * N, [0] * N

    for u in range(1, n + 1):
        dsu[u] = u

    # 注意这里的边向是从 u -> v
    for u in range(1, n + 1):
        v = int(input())
        graph[u] = v
        if v:  # 建立联通块
            dsu[find(u)] = dsu[find(v)]

    # 检查不是基环树的联通块数量
    cnt = 0
    for u in range(1, n + 1):
        root = find(u)
        if graph[root] == 0: cnt += 1

    print(cnt)


dsuCheckCycle()


# TODO: 能否进行记忆化搜索呢？
def memoSearch():
    pass
