N = 5010
n, r = map(int, input().split())
# 保证数据不溢出
r = min(5001, r)
# 前缀和数组
s = [[0] * N for _ in range(N)]
#
w, h = 5001, 5001

# 1. 物品填充
for _ in range(n):
    x, y, v = map(int, input().split())
    s[x][y] += v

# 2. 前缀和处理
for i in range(1, w):
    for j in range(1, h):
        s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]

ans = 0
# 3. 寻找能炸毁的矩形中物品和
for i in range(r, w):
    for j in range(r, h):
        ans = max(ans,
                  s[i][j] - s[i - r][j] - s[i][j - r] + s[i - r][j - r]
                  )

print(ans)
