def ipt(): return map(int, input().split())


def find(u):
    if u != dsu[u]:
        dsu[u] = find(dsu[u])
    return dsu[u]


N, M = int(2e3 + 5), int(1e4 + 5)
n, m = ipt()
edges, dsu = [], [0] * N

# init dsu
for u in range(1, n + 1):
    dsu[u] = u

shrinked_edge_sum = 0
for _ in range(m):
    required, u, v, w = ipt()
    # 缩点操作
    if required == 1:
        dsu[find(u)] = find(v)
        shrinked_edge_sum += w
    else:
        edges.append((u, v, w))

edges.sort(key=lambda e: e[2])
selected_edges_sum = shrinked_edge_sum

for u, v, w in edges:
    u, v = find(u), find(v)
    if u != v:
        dsu[u], selected_edges_sum = v, selected_edges_sum + w

print(selected_edges_sum)
