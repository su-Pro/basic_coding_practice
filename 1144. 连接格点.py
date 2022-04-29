import functools
import sys

sys.setrecursionlimit(10000000)


def ipt(): return map(int, input().split())

@functools.lru_cache(None)
def find(u):
    if dsu[u] != u:
        dsu[u] = find(dsu[u])
    return dsu[u]


N = int(1e3 + 5)
M = N * N
edges, matrix_to_graph, dsu = [], [[0] * N for x in range(N)], [0] * M
n, m = ipt()

# 初始化并查集
for u_num in range(1, n * m):
    dsu[u_num] = u_num

u_start = 1
for x in range(1, n + 1):
    for y in range(1, m + 1):
        matrix_to_graph[x][y], u_start = u_start, u_start + 1

while True:
    try:
        x1, y1, x2, y2 = ipt()
        u, v = find(matrix_to_graph[x1][y1]), find(matrix_to_graph[x2][y2])
        if u != v:
            dsu[u] = v
    except:
        break
# 加边

direction_w, dx, dy = (1, 2), (-1, 0, 1, 0), (0, -1, 0, 1)
for add_edge_direction in range(2):
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            # NOTE: 明明感觉这里的四边循环逻辑不需要写的，每次每点都是一个添加顺序？
            for d in range(4):
                # 保证先加竖边（取决于四条边遍历的方向）
                if d % 2 != add_edge_direction:
                    continue
                nx, ny = x + dx[d], y + dy[d]
                if 0 < nx <= n and 0 < ny <= m:
                    u, v = matrix_to_graph[x][y], matrix_to_graph[nx][ny]
                    # 利用并查集的性质，可以将初始化时处理好的边也加入
                    if u < v:
                        edges.append((u, v, direction_w[add_edge_direction]))

ans = 0
for u, v, w in edges:
    u, v = find(u), find(v)
    if u != v:
        dsu[u], ans = v, ans + w

print(ans)
