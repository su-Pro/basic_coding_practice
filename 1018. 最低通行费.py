N = 105
n = int(input())
g = [list(map(int, input().split())) for x in range(n)]


def smartDP():
    max_value = 100 * N
    f = [[max_value] * N for x in range(N)]
    # 注意这里由于要求最小，和摘花生的处理细节不一致
    f[1][1] = g[0][0]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # S-TODO: 为什么这里要求得两次呢？
                f[i][j] = min(f[i][j], f[i - 1][j] + g[i - 1][j - 1])
                f[i][j] = min(f[i][j], f[i][j - 1] + g[i - 1][j - 1])
    print(f[n][n])


def memoSearch():
    dx,dy = (0,1),(1,0)
    n = int(input())
    g = [list(map(int,input().split())) for _ in range(n)]
    moz = [[0] * N for x in range(N)]
    vt = [[False] * n for _ in range(n)]

    def is_ok(x,y): return 0 <= x < n and 0 <= y < n and not vt[x][y]

    def dfs(x,y):
        # base case:
        if x == n - 1 and y == n - 1: return g[x][y]
        # 最优解
        if moz[x][y]: return moz[x][y]
        case_ans = 100 * 100

        for d in range(2):
            nx,ny = dx[d] + x,dy[d] + y
            if not is_ok(nx,ny): continue
            # 因为存在相反方向,避免打圈，需要用vt来标识
            vt[nx][ny] = True
            case_ans = min(case_ans,dfs(nx,ny))
            vt[nx][ny] = False

        moz[x][y] = case_ans + g[x][y]
        return moz[x][y]

    print(dfs(0,0))


def bruteForce():
    dx, dy = (0, 1), (1, 0)
    vs = [[False] * N for x in range(N)]

    def is_ok(x, y):
        return 0 <= x < n and 0 <= y < n and not vs[x][y]

    def dfs(x, y):
        if x == y == n - 1:
            return g[n - 1][n - 1]
        sub_min = 100 * 100
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not is_ok(nx, ny):
                continue
            vs[nx][ny] = True
            sub_min = min(sub_min, dfs(nx, ny))
            vs[nx][ny] = False
        return sub_min + g[x][y]

    print(dfs(0, 0))

bruteForce()
# memoSearch()
smartDP()
