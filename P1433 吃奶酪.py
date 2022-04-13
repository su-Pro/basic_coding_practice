N = 20
n = int(input())
d = [tuple(map(int, input().split())) for x in range(n)]
# vs = [False] * N
ans = 0
for a in range(n - 1):
    d_min = (200 * 200) + 10
    for b in range(a + 1, n):
        a_x, a_y = d[a]
        b_x, b_y = d[b]
        d_min = min(d_min, abs(a_x * a_x - b_x * b_x)
                    + abs(a_y * a_y - b_y * b_y))
    ans += (d_min * d_min)
print(ans)
