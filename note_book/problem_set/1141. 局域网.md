def ipt(): return map(int, input().split())


def find(u):
    if dsu[u] != u:
        dsu[u] = find(dsu[u])
    return dsu[u]


N, K = 105, 205
edges, dsu = [], [0] * N
n, m = ipt()

for _ in range(m):
    u, v, w = ipt()
    edges.append((u, v, w))

ignored_edge_sum, check_edge_cnt = 0, 0

# 1. 初始化并查集
for i in range(1, n + 1):
    dsu[i] = i

edges.sort(key=lambda e: e[2])

# 2. 选边,统计忽略后的值
for u, v, w in edges:
    u, v = find(u), find(v)
    if u != v:
        dsu[u], check_edge_cnt = v, check_edge_cnt + 1
    else:
        ignored_edge_sum += w
print(ignored_edge_sum)
# NOTE: 这里不能简单认为 check_edge_cnt != n - 1 就一定是错误的，因为有可能是两个环（题意没说清，忽略吧，看测试数据：）
# 6 6
# 1 2 5
# 1 3 4
# 2 3 8
# 4 5 7
# 4 6 2
# 5 6 1
# print(-1 if check_edge_cnt != n - 1 else ignored_edge_sum)
