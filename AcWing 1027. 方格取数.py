N = 11
n = int(input())
g = [[0] * N for x in range(N)]
while True:
    x, y, v = map(int, input().split())
    if x == y == v == 0:
        break
    g[x - 1][y - 1] = v


def memoSearch():
    pass


def bruteForce():
    f = [[
             [
                 [-1] * N for x in range(N)
             ]
         ] * N for x in range(N)]

    def dfs(xa, xb, ya, yb):
        if f[xa][ya][xb][yb] != -1: return f[xa][ya][xb][yb]
        #  TODO: 为什么不加重复计算的逻辑，就爆了呢？
        if xa == xb == ya == yb == n: return 0
        ans = 0
        if xa < n and xb < n:
            ans = max(ans, dfs(xa + 1, xb + 1, ya, yb) +
                      g[xa + 1][ya] + g[xb + 1][yb] - g[xa + 1][ya] * (xa + 1 == xb + 1 and ya == yb))

        if xa < n and yb < n:
            ans = max(ans, dfs(xa + 1, xb, ya, yb + 1) +
                      g[xa + 1][ya] + g[xb][yb + 1] - g[xa + 1][ya] * (xa + 1 == xb and ya == yb + 1))
        if ya < n and xb < n:
            ans = max(ans, dfs(xa, xb + 1, ya + 1, yb) +
                      g[xa][ya + 1] + g[xb + 1][yb] - g[xa][ya + 1] * (xa == xb + 1 and ya + 1 == yb))
        if ya < n and yb < n:
            ans = max(ans, dfs(xa, xb, ya + 1, yb + 1) +
                      g[xa][ya + 1] + g[xb][yb + 1] - g[xa][ya + 1] * (xa == xb and ya + 1 == yb + 1))
        f[xa][ya][xb][yb] = ans
        return ans

    print(dfs(0,0,0,0) + g[0][0])


bruteForce()
