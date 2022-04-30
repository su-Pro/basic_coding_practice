N, k = 105, int(input())
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def depth_first_search(x, y):
    if x == x2 and y == y2:
        return True
    vt[x][y] = True
    # TODO: 是acwing 数据有问题？ 为什么使用can_arrive 这种形式就TLE呢？
    # can_arrive = False
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and not vt[nx][ny] and g[nx][ny] == '.':
            # can_arrive = can_arrive or depth_first_search(nx, ny)
            if depth_first_search(nx, ny):
                return True
    # return can_arrive
    return False


for _ in range(k):
    n = int(input())
    g, vt = [list(input()) for x in range(n)], [
        [False] * N for x in range(N)]
    x1, y1, x2, y2 = map(int, input().split())

    if g[x1][y1] == '#' or g[x2][y2] == '#':
        print('NO')
    else:
        print('YES' if depth_first_search(x1, y1) else "NO")
