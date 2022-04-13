N = 105
n = int(input())
g = [list(map(int, input().split())) for x in range(n)]


def memoSearch():
    dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)
    vs = [[False] * N for x in range(N)]
    memo = [[0] * N for x in range(N)]

    def is_ok(x, y):
        return 0 <= x < n and 0 <= y < n and not vs[x][y]

    def dfs(x, y):
        if x == y == n - 1:
            return g[n][n]
        if memo[x][y] != 0: return memo[x][y]
        sub_min = 100 * 100
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not is_ok(nx, ny): continue
            vs[nx][ny] = True
            sub_min = min(sub_min, dfs(nx, ny))
            vs[nx][ny] = False
        memo[x][y] = sub_min + g[x][y]
        return memo[x][y]

    print(dfs(0, 0))


def bruteForce():
    dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)
    vs = [[False] * N for x in range(N)]

    def is_ok(x, y):
        return 0 <= x < n and 0 <= y < n and not vs[x][y]

    def dfs(x, y):
        if x == y == n - 1:
            return g[n - 1][n - 1]
        sub_min = 100 * 100
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not is_ok(nx, ny): continue
            vs[nx][ny] = True
            sub_min = min(sub_min, dfs(nx, ny))
            vs[nx][ny] = False
        return sub_min + g[x][y]

    print(dfs(0, 0))

memoSearch()
# bruteForce()
