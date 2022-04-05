N = 105
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
f = [[0] * N for x in range(N)]

for i in range(1, n + 1):
    for j in range(0, k + 1):
        if j == a[i]:
            f[i][j] = f[i - 1][j] + 1
        elif j > a[i]:
            f[i][j] = f[i - 1][j] + f[i - 1][j - a[i]]  # 有剩余
        else:  # 不选
            f[i][j] = f[i - 1][j]

print(f[n][k])

#  TODO: 回顾二进制枚举板子 + LC 周赛题
