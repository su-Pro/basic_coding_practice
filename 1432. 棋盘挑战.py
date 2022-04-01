N = 15
n, ans, path, vs_col, vs_deg, vs_undeg = int(input()), 0, [0] * N, [False] * N, [False] * (N * 2), [False] * (N * 2)


def dfs(row):
    global ans
    if row > n:
        ans += 1
        if ans <= 3:
            print(*path[1:n + 1])
        return
    for col in range(1, n + 1):
        if not vs_col[col] and not vs_deg[row + col] and not vs_undeg[col - row + N]:
            # 尝试每种可能
            path[row] = col
            vs_col[col], vs_deg[row + col], vs_undeg[col - row + N] = True, True,True
            dfs(row + 1)
            vs_col[col], vs_deg[row + col], vs_undeg[col - row + N] = False, False, False


dfs(1)
print(ans)
