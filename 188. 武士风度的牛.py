import collections
N = 155
m, n = map(int, input().split())
g, dist = [list(input()) for x in range(n)], [[-1] * N for x in range(N)]

dx, dy = (-1, -1, 1, 1, -2, -2, 2, 2), (-2, 2, 2, -2, -1, 1, 1, -1)


def isOK(
    x, y): return 0 <= x < n and 0 <= y < m and g[x][y] != '*' and dist[x][y] == -1


def bfs(start_x, start_y):
    que = collections.deque()
    que.append((start_x, start_y))
    dist[start_x][start_y] = 0
    while que:
        x, y = que.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if not isOK(nx, ny):
                continue
            dist[nx][ny] = dist[x][y] + 1
            que.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'H':
                return dist[i][j]


for i in range(n):
    for j in range(m):
        if g[i][j] == 'K':
            print(bfs(i, j))
