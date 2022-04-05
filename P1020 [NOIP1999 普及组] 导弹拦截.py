N = 100010
f = [1] * N
a = list(map(int, input().split()))
n = len(a)
a = [-1] + a
for i in range(1, n + 1):
    for j in range(1, i):
        # 为了不让这里取a元素时 - 1，对a 前面进行补0
        if a[j] <= a[i]: continue
        f[i] = max(f[i], f[j] + 1)

print(max(f[:n + 1]))

f = [1] * N
for i in range(1, n + 1):
    for j in range(1, i):
        if a[j] >= a[i]: continue
        f[i] = max(f[i], f[j] + 1)

print(max(f[: n + 1]))
