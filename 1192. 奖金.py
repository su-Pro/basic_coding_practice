import collections

ipt = lambda: map(int, input().split())
N, M = int(1e4 + 5), int(2e4 + 5)
n, m = ipt()

h, e, ne, idx = [0] * N, [0] * M, [0] * M, 0
in_degree = [0] * N


def top_sort_path_sum():
    path_sum, que,check_has_cycle = 0, collections.deque(),0
    for u in range(1, n + 1):
        if in_degree[u] == 0: que.append((100, u))

    while que:
        d, u = que.popleft()
        path_sum += d
        check_has_cycle += 1
        u = h[u]
        while u:
            v = e[u]
            in_degree[v] -= 1
            if in_degree[v] == 0:
                que.append((d + 1, v))
            u = ne[u]
    if check_has_cycle != n:
        return False
    return path_sum

def add(u, v):
    global idx
    idx += 1
    e[idx], ne[idx], h[u] = v, h[u], idx


for _ in range(m):
    u, v = ipt()
    # 低指向高
    add(v, u)
    in_degree[u] += 1

path_sum = top_sort_path_sum()
print('Poor Xed' if not path_sum else path_sum)
