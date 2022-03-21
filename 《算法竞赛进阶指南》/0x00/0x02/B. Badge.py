n = int(input())
pos = [0] + list(map(int, input().split()))


# 对每个定点进行检查
def find(u):
    # 注意，对于每个顶点都有一个全新的检查状况表
    vs = [False] * (n + 1)
    v = u
    while not vs[v]:
        v = pos[v]
        vs[v] = True
    return v


def dfs(u):
    if vs[u]:
        return u
    vs[u] = True
    return dfs(pos[u])


for i in range(1, n + 1):
    # print(find(i))
    vs = [False] * (n + 1)
    print(dfs(i))
