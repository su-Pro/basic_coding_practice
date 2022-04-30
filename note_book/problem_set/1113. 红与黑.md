dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)


def depth_first_search():
    def dfs(x, y):
        vt[x][y] = True
        cnt = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == '.' and not vt[nx][ny]:
                cnt += dfs(nx, ny)
        return cnt
    for i in range(n):
        for j in range(m):
            if g[i][j] == '@':
                print(dfs(i, j))
                break

    # map 函数没有for in 快速，易调试
    # count = 0
    # for v in vt:
    #     count += v.count(True)
    # print(count)


while True:
    m, n = map(int, input().split())  # n行 m列
    if n == 0 and m == 0:
        break
    g, vt = [list(input().strip())
             for i in range(n)], [[False] * m for _ in range(n)]

    depth_first_search()
