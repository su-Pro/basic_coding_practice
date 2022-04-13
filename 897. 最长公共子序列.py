N = 1010
n = int(input())
a, b = [-1] + list(input().split()), [-1] + list(input().split())
f = [[0] * N for x in range(N)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if a[i] != b[j]:
            f[i][j] = max(f[i - 1][j], f[i][j - 1])
        else:
            f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)

print(f[n][n])
