N,  D = int(1e5 + 5), float('inf')
edges, p = [], [0] * N


def ipt(): return map(int, input().split())


def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


def kruskal():
    path_sum = added_edge_cnt = 0
    # 1. 初始化并查集
    for i in range(1, n + 1):
        p[i] = i
    # 2. 排序边
    edges.sort(key=lambda e: e[2])
    # 3. 依次拿取最小边建图
    for u, v, z in edges:
        u, v = find(u), find(v)
        # 用并查集来判断是否联通
        if u != v:
            # 连边
            p[v] = u
            added_edge_cnt += 1
            path_sum += z

    # 4. 检查是否为有效的最小生成树
    return -1 if added_edge_cnt < n - 1 else path_sum


n, m = ipt()
for _ in range(m):
    u, v, z = ipt()
    edges.append((u, v, z))

path_sum = kruskal()

print(path_sum if path_sum != -1 else "impossible")
