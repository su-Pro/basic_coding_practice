import collections

N = 1510
n = int(input())
x1, y1 = map(lambda x: int(x) - 1, input().split())
x2, y2 = map(lambda x: int(x) - 1, input().split())
g = [list(input()) for x in range(n)]
d = [[0] * N for x in range(N)]
dx, dy = (1, 1, -1, -1), (1, -1, -1, 1)


def bsf(x, y):
    que = collections.deque()
    que.append((x, y))
    g[x][y] = '#'
    while que:
        _x, _y = que.popleft()
        for di in range(4):
            nx, ny = _x + dx[di], _y + dy[di]
            # 如何处理滑步？？？？？？？？
            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == '.' and d[nx][ny] == 0:
                d[nx][ny] = d[_x][_y] + 1
                que.append((nx, ny))


bsf(x1, y1)

print(d[x2][y2] if d[x2][y2] != 0 else -1)
