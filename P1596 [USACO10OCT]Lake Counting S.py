import sys
sys.setrecursionlimit(10000000)
n, m = map(int, input().split())
g = [list(input()) for x in range(n)]
cnt = 0
dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)


def dfs(x, y):
    g[x][y] = '.'
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 'W':
            dfs(nx, ny)


for i in range(n):
    for j in range(m):
        if g[i][j] == 'W':
            dfs(i, j)
            cnt += 1

print(cnt)
