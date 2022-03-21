n = int(input())

path = [0] * n
chosen = [False] * (n + 1)

def dfs(h):
    if h == n:
        print(path)
        return
    for i in range(1, n + 1):
        if chosen[i]: continue  # 避免出现同时选了两个1的情况
        path[h] = i  # 覆盖式，不需要恢复现场
        chosen[i] = True
        dfs(h + 1)
        chosen[i] = False

dfs(0)
