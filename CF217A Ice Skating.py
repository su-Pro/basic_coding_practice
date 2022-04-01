N = 100 + 10
fa, x, y, ans = [0] * N, [0] * N, [0] * N, 0


def find(root):
    if root == fa[root]: return root

    fa[root] = find(fa[root])
    return fa[root]


def merge(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: return
    fa[ra] = rb


n = int(input())
for i in range(1, n + 1):
    _x, _y = map(int, input().split())
    x[i] = _x
    y[i] = _y

for i in range(1, n + 1): fa[i] = i

for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        if x[a] == x[b] or y[a] == y[b]:
            merge(a, b)

for i in range(1, n + 1):
    if fa[i] == i: ans += 1

print(str(ans - 1))
