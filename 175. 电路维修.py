import collections
N, maxd = 510, 510 * 510
t = int(input())

char_case = ('\\', '/', '\\', '/')
dx, dy = (-1, -1, 1, 1), (-1, 1, 1, -1)
ix, iy = (-1, -1, 0, 0), (-1, 0, 0, -1)


def isOK(x, y): return 0 <= x <= n and 0 <= y <= m


def bfs():
    que = collections.deque()
    que.append((0, 0))
    dist[0][0] = 0
    while que:
        tx, ty = que.popleft()
        if st[tx][ty]:
            continue
        st[tx][ty] = True
        for i in range(4):
            nx, ny, gx, gy = tx + dx[i], ty + dy[i], tx + ix[i], ty + iy[i]
            # 分case 讨论
            if not isOK(nx, ny):
                continue
            # 距离代价等同于，历史 + (是否需要旋转)
            d = dist[tx][ty] + (char_case[i] != g[gx][gy])
            # 如果有可能更近,因为有的边权是0
            if d >= dist[nx][ny]:
                continue
            dist[nx][ny] = d
            # 边权是0的case,要接着无成本的搜索呐！
            if g[gx][gy] == char_case[i]:
                que.appendleft((nx, ny))
            else:
                que.append((nx, ny))
    return dist[n][m]


while t:
    t -= 1
    n, m = map(int, input().split())
    g, st, dist = [list(input()) for x in range(n)], [
        [False] * N for x in range(N)], [[maxd] * N for x in range(N)]
    count = bfs()
    print(
        'NO SOLUTION' if count == maxd else count
    )
