t = int(input())
N = 105


def smartDP():
    n, m = map(int, input().split())
    f = [[0] * N for x in range(N)]
    g = [list(map(int, input().split())) for x in range(n)]
    # 略过初始化的那行数据
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = max(f[i - 1][j], f[i][j - 1]) + g[i - 1][j - 1]
    print(f[n][m])


def memoSearch():
    n, m = map(int, input().split())
    g = [
        list(map(int, input().split())) for x in range(n)
    ]
    memo = [[0] * N for x in range(N)]

    # 从base-case往前推
    def dfs(x, y):
        if x == n - 1 and y == m - 1:
            return g[x][y]
        if x >= n or y >= m: return 0
        if memo[x][y]: return memo[x][y]
        # 向下和向右取得一个局部最优解
        memo[x][y] = max(dfs(x + 1, y), dfs(x, y + 1)) + g[x][y]
        return memo[x][y]

    print(dfs(0, 0))

    pass


def bruteForce():
    n, m = map(int, input().split())
    g = [
        list(map(int, input().split())) for x in range(n)
    ]

    # 从base-case往前推
    def dfs(x, y):
        if x == n - 1 and y == m - 1:
            return g[x][y]
        if x >= n or y >= m: return 0
        # 向下和向右取得一个局部最优解
        return max(dfs(x + 1, y), dfs(x, y + 1)) + g[x][y]

    print(dfs(0, 0))


for _ in range(t):
    # bruteForce()
    # memoSearch()
    smartDP()
