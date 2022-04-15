import collections

n, N = int(input()), int(1e3 + 5)
g, v = [list(map(int, input().split()))
        for x in range(n)], [[False] * N for x in range(N)]

up_count, lower_count = 0, 0


def isOK(x, y): return 0 <= x < n and 0 <= y < n


def bfs(x, y):
    que = collections.deque()
    que.append((x, y))
    v[x][y] = True
    has_up, has_lower = False, False

    while que:
        tx, ty = que.popleft()
        for nx in range(tx - 1, (tx + 1) + 1):
            for ny in range(ty - 1, (ty + 1) + 1):
                if nx == tx and ny == ty:
                    continue
                if not isOK(nx, ny):
                    continue
                # 检查山峰还是山谷
                if g[nx][ny] != g[tx][ty]:
                    if g[tx][ty] > g[nx][ny]:
                        has_up = True
                    else:
                        has_lower = True
                # 一定是连通关系，因为过了上面的case
                elif not v[nx][ny]:
                    que.append((nx, ny))
                    v[nx][ny] = True
    return has_up, has_lower


# 遍历所有的格子
for i in range(n):
    for j in range(n):
        # 已经被检查过
        if v[i][j]:
            continue
        has_up, has_lower = bfs(i, j)
        if not has_lower:
            up_count += 1
        if not has_up:
            lower_count += 1

print(up_count, lower_count)
