N = int(1e5) + 10
M = N * 2 + 10
# 之所以为了初始化到最大范围，是为了方便初始化临街表
h, to, ne, idx = [0] * N, [0] * M, [0] * M, 0
st = [False] * N
ans = N

def add(v, u):
    global idx
    idx += 1
    to[idx] = u
    ne[idx] = h[v]
    h[v] = idx

def dfs(u):
    global ans
    size, sum = 0, 1
    st[u] = True
    i = h[u]
    while i:
        node = to[i]
        i = ne[i]
        if st[node]: continue
        s = dfs(node)
        size = max(size, s)
        sum += s
    size = max(size, n - sum)
    ans = min(size, ans)
    return sum

n = int(input())

for _ in range(n - 1):
    u, v = map(int, input().split())
    add(u, v)
    add(v, u)
dfs(1)