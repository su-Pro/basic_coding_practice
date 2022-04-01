N, k = map(int, input().split())
a = list(map(int, input().split()))

# 1. 求前缀和
s = [0] + [0] * N
a = [0] + a
for i in range(1, N + 1):
    s[i] = s[i - 1] + a[i]

# 2.处理询问
for _ in range(k):
    l, r = map(int, input().split())
    print(s[r] - s[l - 1])
