import math

N, n, D = 155, int(input()), float('inf')
point_xy = [tuple(map(int, input().split())) for x in range(n)]
g, dist = [list(map(int, input())) for x in range(n)], [[D] * N for x in range(N)]


def get_distance(u, v):
    ux, uy = point_xy[u]
    vx, vy = point_xy[v]
    deta_x, deta_y = ux - vx, uy - vy
    return math.sqrt(deta_x * deta_x + deta_y * deta_y)


# 1. 初始化dist中的欧几里得距离
for u in range(n):
    for v in range(n):
        if u == v:
            dist[u][v] = 0
        elif g[u][v] == 1:
            dist[u][v] = get_distance(u, v)

# 2. 求得各个连通块点与点之间的最短距离
for k in range(n):
    for u in range(n):
        for v in range(n):
            dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

# 3. 计算case1 和 case2的值,取max即为答案
case_one_d, case_two_d = 0, D

# 3.1 计算每个点距离联通块中最远的距离是多少
max_dist = [0.0] * N
for u in range(n):
    for v in range(n):
        if dist[u][v] != D:
            max_dist[u] = max(max_dist[u], dist[u][v])
        case_one_d = max(case_one_d, max_dist[u])

for u in range(n):
    for v in range(n):
        # NOTE: 只有两点不联通（不在一个块中，才可连边）
        if dist[u][v] == D:
            case_two_d = min(case_two_d, max_dist[u] + max_dist[v] + get_distance(u, v))

# TODO: 为什么这里是取max逻辑而不是min呢？？？
print('%.6f' % (max(case_one_d, case_two_d)))
