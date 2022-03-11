n = int(input())


def bitmask():
    # 枚举所有的可能性
    for p in range(1 << n):
        s = ""
        # 依次检查当前位，判断是否需要当前位所代表的值
        # 一共检查n位，从低到高
        for i in range(n):
            if p >> i & 1:
                # 注意这里的错位情况，idx -> 0  <=> ans -> 1
                s += str(i + 1) + ' '
        print(s)


def dfs(h, p):
    if h == n:
        print(p)
        return
    dfs(h + 1, p + str(h + 1) + ' ')
    dfs(h + 1, p)


dfs(0, '')
