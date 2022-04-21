N = 105
n = int(input())
g = [list(map(int, input().split())) for x in range(n)]


def smartDP():
    max_value = 100 * N
    f = [[max_value] * N for x in range(N)]
    f[1][1] = g[0][0]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 特殊处理边界:第一行和第一列
            if i > 1:
                f[i][j] = min(f[i][j], f[i - 1][j] + g[i - 1][j - 1])
            if j > 1:
                f[i][j] = min(f[i][j], f[i][j - 1] + g[i - 1][j - 1])
    print(f[n][n])


def memoSearch():
    dx, dy = (0, 1), (1, 0)
    vs = [[False] * N for x in range(N)]
    memo = [[0] * N for x in range(N)]

    def is_ok(x, y):
        return 0 <= x < n and 0 <= y < n and not vs[x][y]

    def dfs(x, y):
        if x == y == n - 1:
            return g[n - 1][n - 1]
        if memo[x][y] != 0:
            return memo[x][y]
        sub_min = 100 * 100
        for d in range(2):
            nx, ny = x + dx[d], y + dy[d]
            if not is_ok(nx, ny):
                continue
            vs[nx][ny] = True
            sub_min = min(sub_min, dfs(nx, ny))
            vs[nx][ny] = False
        memo[x][y] = sub_min + g[x][y]
        return memo[x][y]

    print(dfs(0, 0))


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


# memoSearch()
# bruteForce()
smartDP()
