import collections

n, m = map(int, input().split())
g = [
    tuple(map(int, input())) for x in range(n)
]
d_g = [[-1] * m for x in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def isOk(x, y):
    return 0 <= x < n and 0 <= y < m and d_g[x][y] == -1 and g[x][y] == 0


def bfs():
    que = collections.deque()
    for x in range(n):
        for y in range(m):
            if g[x][y] == 1:
                que.append((x, y))
                d_g[x][y] = 0
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if isOk(nx, ny):
                d_g[nx][ny] = d_g[x][y] + 1
                que.append((nx, ny))


bfs()
for row in d_g:
    print(*row)
