n = int(input())
N = 105
vs = [[False] * N for x in range(N)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            vs[x][y] = True

ans = 0
for row in vs:
    ans += row.count(True)
print(ans)
