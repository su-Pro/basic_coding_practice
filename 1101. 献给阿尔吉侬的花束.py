import collections

N, M = 210, 210
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)


def do():
    def bfs(i, j):
        dist = [[0] * N for x in range(M)]
        q = collections.deque()
        q.append((i, j))
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#' and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    if g[nx][ny] == 'E': return dist[nx][ny]
                    q.append((nx, ny))
        return -1

    n, m = map(int, input().split())
    g = [list(input()) for x in range(n)]
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'S':
                return bfs(i, j)


for _ in range(int(input())):
    count = do()
    print(count if count != -1 else 'oop!')
