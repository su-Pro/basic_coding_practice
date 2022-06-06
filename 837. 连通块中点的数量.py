def find(u):
    if dsu[u] != u:
        dsu[u] = find(dsu[u])
    return dsu[u]


n, k = map(int, input().split())
dsu, dsu_size = [0] * (n + 1), [1] * (n + 1)

# 1. 初始化并查集
for u in range(1, n + 1):
    dsu[u] = u

# 2. 处理询问

for _ in range(k):
    line = input().split()
    opt = line[0]

    # 获取当前a 所在联通块的大小
    if opt == 'Q2':
        u = int(line[1])
        print(dsu_size[find(u)])
        continue
    u, v = int(line[1]), int(line[2])
    # 检查u，v 是否在一个集合中
    if opt == 'Q1':
        u, v = find(u), find(v)
        print("Yes" if u == v else "No")
        continue

    # 建立联通块，u <-> v
    if opt == 'C':
        u, v = find(u), find(v)
        # Note: 如果两个数据明确说u,v 可能是相同点，此时不要再去盲目合并...
        if u == v: continue
        dsu_size[v] += dsu_size[u]
        dsu[u] = v
        continue
