dx, dy = (0, 2, 1, -1, -2, -2, -1, 1, 2), \
         (0, 1, 2, 2, 1, -1, -2, -2, -1)
N = 25


def simple():
    t_x, t_y, a, b = map(int, input().split())
    mx, my = (1, 0), (0, 1)
    ans = 0

    def ok(x, y):
        if x > t_x or y > t_y: return False
        for i in range(9):
            horse_x, horse_y = a + dx[i], b + dy[i]
            if x == horse_x and y == horse_y: return False
        return True

    def dfs(x, y):
        if x == t_x and y == t_y:
            global ans
            ans += 1
            return

        # moving!
        for i in range(2):
            nx, ny = mx[i] + x, my[i] + y
            if not ok(nx, ny): continue
            dfs(nx, ny)

    dfs(0, 0)

    print(ans)


def smart():
    n, m, a, b = map(int, input().split())
    f = [[0] * N for x in range(N)]

    for i in range(9):
        na, nb = a + dx[i], b + dy[i]
        f[na][nb] = -1

    if f[0][0] == -1:
        print(0)
        return
    else:
        f[0][0] = 1

    for i in range(n + 1):
        for j in range(m + 1):
            if (i == 0 and j == 0) or f[i][j] == -1: continue
            u_cnt = 0 if i == 0 or f[i - 1][j] == -1 else f[i - 1][j]
            l_cnt = 0 if j == 0 or f[i][j - 1] == -1 else f[i][j - 1]
            f[i][j] = l_cnt + u_cnt

    print(f[n][m])


smart()
