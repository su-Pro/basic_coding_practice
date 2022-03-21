def floodFill():
    import sys

    sys.setrecursionlimit(2 ** 30)

    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    N, M = 1010, 1010
    grid, vt, ans = [], [[False] * M for _ in range(N)], 0
    n, m = map(int, input().split())
    for _ in range(n):
        grid.append(list(input()))

    def dfs(x, y):
        if not 0 <= x < n or not 0 <= y < m or vt[x][y] or grid[x][y] != '.': return 0
        cnt = 1
        vt[x][y] = True
        for d in range(4):
            cnt += dfs(x + dx[d], y + dy[d])
        return cnt

    for x in range(n):
        for y in range(m):
            if dfs(x, y) > 0: ans += 1
    print(ans)


def Uset ():
    pass