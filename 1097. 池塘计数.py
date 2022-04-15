import collections
N = int(1e3 + 10)
n, m = map(int, input().split())
g = [
    list(input()) for x in range(n)
]
dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)


def isOK(
    x, y): return 0 <= x < n and 0 <= y < m and g[x][y] == 'W' and not vs[x][y]


def bfs(x, y):
    que = collections.deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if isOK(nx, ny):
                que.append((nx, ny))
                vs[nx][ny] = True


cnt, vs = 0, [[False] * m for x in range(n)]
for i in range(n):
    for j in range(m):
        if g[i][j] == 'W' and not vs[i][j]:
            vs[i][j] = True
            bfs(i, j)
            cnt += 1

print(cnt)
