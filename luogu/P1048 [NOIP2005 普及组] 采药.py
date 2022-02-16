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

