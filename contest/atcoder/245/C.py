N, K = map(int, input().split())
a, b = [0] + list(map(int, input().split())), [0] + \
    list(map(int, input().split()))
adp, bdp = [False] * (N + 1), [False] * (N + 1),

adp[1], bdp[1] = True, True
for i in range(2, N + 1):
    if adp[i - 1]:
        if abs(a[i] - a[i - 1]) <= K:
            adp[i] = True
        if abs(b[i] - a[i - 1]) <= K:
            bdp[i] = True
    if bdp[i - 1]:
        if abs(a[i] - b[i - 1]) <= K:
            adp[i] = True
        if abs(b[i] - b[i - 1]) <= K:
            bdp[i] = True

print("Yes") if (adp[N] or bdp[N]) else print("No")
