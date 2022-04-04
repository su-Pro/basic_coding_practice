N, K = map(int, input().split())
a, b = [0] + list(map(int, input().split())), [0] + list(map(int, input().split()))
fa, fb = [False] * (N + 1), [False] * (N + 1)

fa[1] = fb[1] = True
for i in range(2, N + 1):
    if fa[i - 1]:
        if abs(a[i - 1] - a[i]) <= K: fa[i] = True
        if abs(a[i - 1] - b[i]) <= K: fb[i] = True
    if fb[i - 1]:
        if abs(b[i - 1] - a[i]) <= K: fa[i] = True
        if abs(b[i - 1] - b[i]) <= K: fb[i] = True

print('Yes' if fa[N] or fb[N] else 'No')
