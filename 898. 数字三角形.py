N = 510
n = int(input())
g = [list(map(int, input().split())) for x in range(n)]


def smartDp():
    f = [[float('inf')] * N for x in range(N)]
    # 初始化函数边界
    for j in range(1, n + 1):
        f[n][j] = g[n - 1][j - 1]
    # 递推函数
    for i in range(n - 1, 0, -1):
        for j in range(i, 0, -1):
            f[i][j] = max(f[i + 1][j], f[i + 1][j + 1]) + g[i - 1][j - 1]
    print(f[1][1])


smartDp()


def memorySearch():
    memo = [[0] * n for x in range(n)]

    def dfs(x, y):
        if x == n - 1:
            return g[x][y]
        if memo[x][y] != 0:
            return memo[x][y]
        memo[x][y] = g[x][y] + max(dfs(x + 1, y), dfs(x + 1, y + 1))
        return memo[x][y]

    print(dfs(0, 0))


def bruteForce():
    def dfs(x, y):
        if x == n - 1:
            return g[x][y]
        return g[x][y] + max(dfs(x + 1, y), dfs(x + 1, y + 1))

    print(
        dfs(0, 0)
    )
