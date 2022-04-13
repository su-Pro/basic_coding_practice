def bruteForce():
    T, M = map(int, input().split())
    t, w = [], []

    for _ in range(M):
        _t, _w = map(int, input().split())
        t.append(_t)
        w.append(_w)

    res = 0

    def dfs(level, T):
        if level == M:
            return 0

        elif t[level] > T:
            res = dfs(level + 1, T)
        else:
            res = max(dfs(level + 1, T), dfs(level + 1, T - t[level]) + w[level])

        return res

    print(dfs(0, T))


def smartDP():
    N, V = 105, 1010
    v, n = map(int, input().split())
    v_w = [(-1,-1)] + [
        tuple(map(int, input().split())) for x in range(n)
    ]
    f = [[0] * V for x in range(N)]
    for i in range(1, n + 1):
        for j in range(0, v + 1):
            f[i][j] = f[i - 1][j]
            if j >= v_w[i][0]:
                f[i][j] = max(f[i][j],f[i - 1][j - v_w[i][0]] + v_w[i][1])

    print(f[n][v])

smartDP()