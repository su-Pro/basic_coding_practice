import collections

N = 410
n, m, a, b = map(int, input().split())
d_vs = [[-1] * N for x in range(N)]
dx, dy = (2, 2, -2, -2, 1, 1, -1, -1), (-1, 1, -1, 1, -2, 2, -2, 2)
# init 距离
d_vs[a][b] = 0


def ok(na, nb):
    return d_vs[na][nb] == -1 and 1 <= na <= n and 1 <= nb <= m


def bfs(x, y):
    que = collections.deque()
    que.append((x, y))
    while que:
        a, b = que.popleft()
        for d in range(8):
            na, nb = a + dx[d], b + dy[d]
            if not ok(na, nb): continue
            que.append((na, nb))
            d_vs[na][nb] = d_vs[a][b] + 1


bfs(a, b)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print("%-5d" % d_vs[i][j],end='')
    print()
