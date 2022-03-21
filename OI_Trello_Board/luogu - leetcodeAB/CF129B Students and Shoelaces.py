I = lambda: map(int, input().split())
n, m = I()
g = [[0] * n for _ in range(n)]
# 建立边
for _ in range(m):
    u, v = I()
    g[u - 1][v - 1] = 1
    g[v - 1][u - 1] = 1

kicked_time = 0
while True:
    # 统计所有度为1的定点集合
    s = [i for i in range(n) if sum(g[i]) == 1]
    if len(s) == 0: break
    # 踢出s中的节点，并更新他的度
    for _s in s:
        for i in range(n):
            # 删除一组边
            g[_s][i], g[i][_s] = 0, 0
    kicked_time += 1
print(kicked_time)
