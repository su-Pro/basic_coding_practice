W, H = 25, 25
dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)


def dfs(x, y):
    vs[x][y] = True
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < w and 0 <= ny < h and g[nx][ny] != '#' and not vs[nx][ny]:
            dfs(nx, ny)


while True:
    h, w = map(int, input().split())
    if w == h == 0: break
    vs, g = [[False] * H for x in range(W)], [list(input()) for x in range(w)]
    for x in range(w):
        for y in range(h):
            if g[x][y] == '@':
                dfs(x, y)
    print(
        sum(vs, []).count(True)
    )
