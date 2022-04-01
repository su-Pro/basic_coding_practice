N = int(input())
Ax = list(map(int, input().split()))
Ay = list(map(int, input().split()))

ans = 0

# 依次检查点A 和 点B，求距离，打擂台
# 注意 点B 一定是在A之后的点，不要重复了
for a in range(N):
    for b in range(a + 1, N):
        dx = Ax[a] - Ax[b]
        dy = Ay[a] - Ay[b]
        ans = max(ans, dx * dx + dy * dy)

print(ans)
