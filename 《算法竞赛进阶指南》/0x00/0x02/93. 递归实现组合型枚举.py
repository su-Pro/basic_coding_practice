n, m = map(int, input().split())
chosen = []

def dfs(h):
    # 对非法问题进行剪枝操作
    if len(chosen) > m or len(chosen) + (n - h) < m: return

    if h == n:
        return print(*chosen)

    chosen.append(str(h + 1))
    dfs(h + 1)
    chosen.pop()
    dfs(h + 1)

dfs(0)
