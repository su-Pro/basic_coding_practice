N = 105
p, edges = [0] * N, []


def ipt(): return map(int, input().split())


def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


def kruskal():
    path_sum = 0
    for i in range(1, n + 1):
        p[i] = i
    edges.sort(key=lambda edge: edge[2])
    for u, v, z in edges:
        u, v = find(u), find(v)
        if u != v:
            p[v] = u
            # 这里的z，是属于最小生成树的
        else:
            # 这里的z，是不属于最小生树的，要被去掉的边权
            path_sum += z
    return path_sum


n, m = ipt()
for _ in range(m):
    u, v, z = ipt()
    edges.append((u, v, z))

print(kruskal())
