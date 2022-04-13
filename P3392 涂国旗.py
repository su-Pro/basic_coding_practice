N = 55
n, m = map(int, input().split())
g = [
    list(input()) for x in range(n)
]
ans = 3 * N

# 定义三个段： 0 ~ i => w
# i + 1 ~ j => b
# j + 1 ~ n => R

w, b, r = [0] * N, [0] * N, [0] * N

for i in range(1, n + 1):
    w[i] = w[i - 1] + m - g[i - 1].count("W")
    b[i] = b[i - 1] + m - g[i - 1].count("B")
    r[i] = r[i - 1] + m - g[i - 1].count("R")

for i in range(1, n - 1):
    for j in range(i + 1, n + 1):
        ans = min(
            ans,
            w[i] + (b[j] - b[i + 1 - 1]) + (r[n] - r[j + 1 - 1])
        )
print(ans)
