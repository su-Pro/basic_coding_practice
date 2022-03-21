n, m = map(int, input().split())
g = [list(input()) for i in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def placeDog(x, y):
    global g
    # 检查四个方向
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if not 0 <= nx < n or not 0 <= ny < m:
            continue
        if g[nx][ny] == 'W':
            return False
        if g[nx][ny] == '.':
            g[nx][ny] = 'D'
    return True


def solve():
    for x in range(n):
        for y in range(m):
            if g[x][y] != 'S':
                continue
            if not placeDog(x, y):
                return False
    return True


if solve():
    print("Yes")
    for row in g:
        print("".join(row), end="\n")
else:
    print("No")
