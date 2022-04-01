import collections

N, M = 110, 110
d = [[0] * M for x in range(N)]
n, m = map(int, input().split())
g = [list(map(int, input().split())) for x in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)


def bfs(x, y):
    que = collections.deque()
    que.append((x, y))
    while que:
        ux, uy = que.popleft()
        for i in range(4):
            vx, vy = ux + dx[i], uy + dy[i]
            if 0 <= vx < n and 0 <= vy < m and g[vx][vy] == 0 and d[vx][vy] == 0:
                d[vx][vy] = d[ux][uy] + 1
                que.append((vx, vy))

bfs(0, 0)

print(d[n - 1][m - 1])
