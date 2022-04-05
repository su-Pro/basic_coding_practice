V = 20000 + 10
v = int(input())
n = int(input())
w_v = [0]
f = [0] * V
for _ in range(n):
    w_v.append(int(input()))

for i in range(1, n + 1):
    for j in range(v, w_v[i] - 1, -1):
        f[j] = max(f[j], f[j - w_v[i]] + w_v[i])

print(v - f[v])
