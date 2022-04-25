N = 10
t = int(input())
dx, dy = (-1, -2, -2, -1, 1, 2, 2, 1), (-2, -1, 1, 2, 2, 1, -1, -2)
cnt = 0


def depth_first_search(x, y, cur_arrived_cnt):
    if cur_arrived_cnt == n * m:
        global cnt
        cnt += 1
        return

    vt[x][y] = True
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not vt[nx][ny]:
            depth_first_search(nx, ny, cur_arrived_cnt + 1)
    # 之所以把这个回溯放在for循环外面，是因为：
    # 在这个点上，能跳的所有位置属于一个棋牌状态
    vt[x][y] = False


for _ in range(t):
    n, m, x, y = map(int, input().split())
    vt = [[False] * N for x in range(N)]
    cnt = 0
    depth_first_search(x, y, 1)
    print(cnt)
