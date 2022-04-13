N = 10
n, m, k = map(int, input().split())
sx, sy, fx, fy = map(int, input().split())
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
roadblock, vs = set(), [[False] * N for x in range(N)]
for _ in range(k):
    x, y = map(int, input().split())
    roadblock.add((x, y))

ans = 0


def ok(x, y):
    return 1 <= x <= n and 1 <= y <= m and (x, y) not in roadblock and not vs[x][y]


def dfs(x, y):
    if x == fx and y == fy:
        global ans
        ans += 1
        return
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if not ok(nx, ny):
            continue
        vs[nx][ny] = True
        dfs(nx, ny)
        vs[nx][ny] = False

# 一定记得将入口进行标记！
roadblock.add((sx, sy))
dfs(sx, sy)
print(ans)
