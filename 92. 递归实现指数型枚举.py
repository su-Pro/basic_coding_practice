n = int(input())


def bitmask():
    for i in range(1 << n):  # 枚举所有可能性
        path = []
        for p in range(n):  # 检查每一位
            if not (1 & i >> p): continue
            path.append(p)
        print(path)


def dfs(h, path):
    if h == n:
        print(path)
        return
    # 使用原始值就不需要对状态进行回溯，层隔离
    # 典型的 "加 或 不加"
    dfs(h + 1, path)
    dfs(h + 1, path + str(h + 1) + ' ')

# dfs(0, '')
# bitmask()
