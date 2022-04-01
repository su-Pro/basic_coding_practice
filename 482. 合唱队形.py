N = 100 + 5
n, a = int(input()), list(map(int, input().split()))
a = [0] + a
f_l, f_r, ans = [1] * N, [1] * N, 0

for i in range(1, n + 1):
    for j in range(1, i):
        if a[j] < a[i]:
            f_l[i] = max(f_l[i], f_l[j] + 1)

for i in range(n, 0, -1):
    for j in range(n, i, -1):
        if a[j] < a[i]:
            f_r[i] = max(f_r[i], f_r[j] + 1)

for i in range(1, n + 1):
    ans = max(ans, f_l[i] + f_r[i] - 1)

print(n - ans)
