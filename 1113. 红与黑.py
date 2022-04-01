dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
m, n = map(int, input().split())  # n行 m列
g, vs = [list(input().strip())
         for i in range(n)], [[False] * m for _ in range(n)]
input()


def dfs(x, y):
    vs[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not vs[nx][ny] and g[nx][ny] == '.':
            dfs(nx, ny)


sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '@':
            sx = i
            sy = j
            break
dfs(sx, sy)
count = 0
for v in vs:
    count += v.count(True)
print(count)
