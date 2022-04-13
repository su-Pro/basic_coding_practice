N = 25
n, a = int(input()), list(input())
g, vs = [[False] * N for x in range(N)], [False] * N

# build edge
for u in range(n - 1):
    for v in tuple(map(int, input().split())):
        g[u][v] = True


def non_path(u):
    # 还有节点并且节点没有被搜过呢
    for i in range(n):
        if g[u][i] and not vs[i]: return False
    return True


def dfs(u, path_sum, searched_count):
    # 判断是否要更新当前的路径
    if non_path(u):
        global ans, ans_path
        if path_sum <= ans: return
        ans = path_sum
        ans_path = path[:searched_count + 1]
    for i in range(n):
        if not g[u][i] and vs[i]: continue
        vs[i] = True
        dfs(i, path_sum + a[i], searched_count + 1)
        vs[i] = False


path, ans, ans_path = [0] * N, 0, None
# 从任意一处开始搜索
for i in range(n):
    vs[i] = True
    dfs(i, a[i], 1)
    vs[i] = False

print(ans, ans_path)
