n = int(input())
p = [int(input()) - 1 for _ in range(n)]


def smartWalkerGraph():
    maxH = 0
    # 以每个节点当作叶节点，去求最高度
    for i in range(n):
        h = 1
        u = p[i]
        while u != -2:
            h += 1
            u = p[u]
        maxH = max(h, maxH)

    print(maxH)


def simpleBuildGraph():
    maxH = 0

    g = [[] for i in range(n)]

    for i in range(n):
        if p[i] != -2:
            g[p[i]].append(i)

    def dfs(u, h):
        global maxH
        if h > maxH: maxH = h
        for vv in g[u]:
            dfs(vv, h + 1)

    for i in range(n):
        if p[i] == -2:
            dfs(i, 1)

    print(maxH)


smartWalkerGraph()
