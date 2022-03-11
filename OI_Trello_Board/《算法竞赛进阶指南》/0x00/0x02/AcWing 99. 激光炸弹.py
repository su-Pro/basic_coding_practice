N = 5010
s = [[0] * N for _ in range(N)]
n, r = map(int, input().split())
# 为什么这里要定义最大边界r 和 w，h 呢？
r = min(5001, r)
w, h = 5001, 5001

for _ in range(n):
    i, j, v = map(int, input().split())
    s[i + 1][j + 1] += v

# 前缀求和
for i in range(1, w + 1):
    for j in range(1, h + 1):
        s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]

# 求所有可能的矩形面积
ans = 0
for i in range(r, w + 1):
    for j in range(r, h + 1):
        ans = max(
            ans,
            s[i][j] - s[i - r][j] - s[i][j - r] + s[i - r][j - r]
        )

print(ans)
