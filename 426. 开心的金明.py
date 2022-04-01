M, V = 30, 30000 + 10
f = [[0] * V for x in range(M)]
v, m = map(int, input().split())
# 0 -> v 1 -> p
a = [tuple(map(int, input().split())) for x in range(m)]

for i in range(1, m + 1):
    for j in range(1, v + 1):
        f[i][j] = f[i - 1][j]
        _v, _p = a[i - 1]
        if _v <= j:
            f[i][j] = max(f[i][j], f[i - 1][j - _v] + _v * _p)

print(f[m][v])
