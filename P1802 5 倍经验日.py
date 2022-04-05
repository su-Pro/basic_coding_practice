N = 1000 + 10
n, k = map(int, input().split())
f = [0] * N
w, v = [0], [0]
initial_sum = 0
for _ in range(n):
    _l, _w, _v = map(int, input().split())
    w.append(_w - _l)
    v.append(_v)
    initial_sum += _l

for i in range(1, n + 1):
    for j in range(k, v[i] - 1, -1):
        f[j] = max(f[j], f[j - v[i]] + w[i])

print(5 * (f[k] + initial_sum))
