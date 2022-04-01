import sys
N = 15
n = int(input())
vs_col, vs_deg, vs_un_deg = [False] * N, [False] * 2 * N, [False] * 2 * N
path, cnt = [0] * n, 0
sys.setrecursionlimit(10000000)


def notOk(x, y):
    return vs_col[y] or vs_deg[y - x + n] or vs_un_deg[y + x]


def dfs(x):
    global cnt
    if x >= n:
        cnt += 1
        if cnt <= 3: print(*map(lambda x: x + 1, path))
        return
    for y in range(n):
        if notOk(x, y): continue
        # try put queue in every col -> y
        path[x] = y
        vs_col[y] = vs_deg[y - x + n] = vs_un_deg[y + x] = True
        dfs(x + 1)
        vs_col[y] = vs_deg[y - x + n] = vs_un_deg[y + x] = False


dfs(0)
print(cnt)
