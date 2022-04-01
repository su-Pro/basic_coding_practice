n, m = map(int, input().split())
vs = [False] * n
for _ in range(m):
    u, v = map(lambda v: int(v) - 1, input().split())
    vs[u] = True
    vs[v] = True

rot = 0
for i in range(1, n + 1):
    if vs[i - 1]: continue
    rot = i
    break

print(n - 1)

for i in range(1, n + 1):
    if i != rot:
        print(str(i) + ' ' + str(rot))
