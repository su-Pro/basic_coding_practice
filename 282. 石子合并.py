N = 310
n = int(input())
s = [0] + list(map(int, input().split()))
f = [[0] * N for x in range(N)]

# prefix
for i in range(1, len(s)):
    s[i] += s[i - 1]

# 枚举区间大小
for interval in range(2, n + 1):
    # 枚举区间的左右边界
    for l in range(1, (n - interval + 1) + 1):
        r = l + interval - 1
        # 枚举可以划分为两段儿的k
        f[l][r] = int(1e9)
        for k in range(l, r):
            f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + s[r] - s[l - 1])

print(f[1][n])
