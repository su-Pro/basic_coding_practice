def dfsSimilar():
    N = 100 + 10
    t = int(input())

    dx, dy = (0, 1, 0, -1, -1, 1, -1, 1), (1, 0, -1, 0, 1, 1, -1, -1)

    def dfs(x, y):
        vs[x][y] = True
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 2 and 0 <= ny < c and grid[nx][ny] == '0' and not vs[nx][ny]:
                dfs(nx, ny)

    for _ in range(t):
        c = int(input())
        grid, vs = [], [[False] * c for _ in range(2)]
        for __ in range(2):
            grid.append(list(input()))
        dfs(0, 0)
        print("YES" if vs[1][c - 1] else "NO")


def smart():
    t = int(input())
    for _ in range(t):
        g = []
        col = int(input())
        for __ in range(2):
            g.append(list(input()))
        # 只要有一列全部为1，则一定过不去
        flag = True
        for check_c in range(col):
            if g[0][check_c] == '1' and g[1][check_c] == '1':
                flag = False
                break
        print("YES" if flag else "NO")


smart()
