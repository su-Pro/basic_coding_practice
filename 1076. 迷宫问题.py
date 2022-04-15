import collections
N, n = int(1e3 + 5), int(input())
g, dist = [list(input().split())
           for x in range(n)], [[-1] * N for x in range(N)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def isOK(
    x, y): return 0 <= x < n and 0 <= y < n and dist[x][y] == -1 and g[x][y] == '0'


def forward_print():
    x, y = n - 1, n - 1
    path = []
    while x != -1 and y != -1:
        path.append((x, y))
        x, y = dist[x][y]
    for p in path[::-1]:
        print(*p)


def bfs():
    que = collections.deque()
    que.append((0, 0))
    dist[0][0] = (-1, -1)
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not isOK(nx, ny):
                continue
            dist[nx][ny] = (x, y)
            que.append((nx, ny))


bfs()
forward_print()
