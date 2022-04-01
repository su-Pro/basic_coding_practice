n, m = map(int, input().split())
g = [[0] * n for i in range(n)]
c = map(int, input().split())


def add(v, u):
    global g
    g[v].append(u)
    g[u].append(v)


for _ in range(m):
    u, v = map(lambda v: int(v) - 1, input().split())
    add(u, v)
    cnt = sum(c)
    for v, uu in enumerate(g):
        vs = [False] * n
        minValue = c[v]
        vs[v] = True
        if not uu:
            cnt -= minValue
            continue
        # 遍历邻居，找到最小的，并且cnt全部减去不是最小的
        for u in uu:
            if vs[u]: continue
            vs[u] = True
            cnt -= c[u]
