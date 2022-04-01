N = 310

dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)

def do():
    def dfs(x, y):
        # correct reduce
        can_go = vs[x][y] == 0
        vs[x][y] = -1
        # need turn 0 to -1
        if not can_go: return
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and vs[nx][ny] != -1:
                dfs(nx, ny)

    n = int(input())
    vs, g = [[False] * N for x in range(N)], [list(input()) for x in range(n)]
    # 1. init g
    for i in range(n):
        for j in range(n):
            if g[i][j] == '*':
                vs[i][j] = -1
            else:
                vs[i][j] = 0
                for d in range(8):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < n and 0 <= nj < n and g[ni][nj] == '*':
                        vs[i][j] += 1
    # 2. count how many zero pos
    cnt = 0
    for i in range(n):
        for j in range(n):
            if vs[i][j] == 0:
                dfs(i, j)
                cnt += 1

    # 3. add near has mines pos
    for i in range(n):
        for j in range(n):
            if vs[i][j] != -1:
                cnt += 1

    return cnt


for _ in range(int(input())):
    print(f'Case #{_ + 1}: {do()}')
