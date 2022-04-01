N = 1010
n = int(input())
f = [0] * (n + 1)
a = [0] + list(map(int, input().split()))
ans = float('-inf')

for i in range(2, n + 1):
    for k in range(1,i):
        if a[k] < a[i]: f[i] = max(f[i], f[k] + 1)
    ans = max(f[i], ans)

print(ans)
