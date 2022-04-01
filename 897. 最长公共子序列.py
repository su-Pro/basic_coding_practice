N = 1010
n, m = map(int, input().split())
s1, s2 = "x" + input(), "x" + input()
f = [[0] * N for x in range(N)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        f[i][j] = max(
            f[i - 1][j],
            f[i][j - 1],
        )
        if s1[i] == s2[j]:
            f[i][j] = max(f[i][j],f[i - 1][j - 1] + 1)
print(
    f[n][m]
)
