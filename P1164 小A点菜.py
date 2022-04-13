N, K = 105, 10010
f = [[0] * K for x in range(N)]
n, k = map(int, input().split())
a = []
while not len(a) >= n:
    t = [int(x) for x in input().split()]
    a.extend(t)
a.insert(0, 0)
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j == a[i]:
            f[i][j] = f[i - 1][j] + 1
        elif j > a[i]:
            f[i][j] = f[i - 1][j] + f[i - 1][j - a[i]]  # 有剩余
        else:  # 不选
            f[i][j] = f[i - 1][j]

print(f[n][k])

#  TODO: 回顾二进制枚举板子 + LC 周赛题
