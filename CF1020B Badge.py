n = int(input())
vs = [False] * (n + 1)
a = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    vs[i] = True
    pos = a[i]
    while not vs[pos]:
        vs[pos] = True
        pos = a[pos]
    print(pos, end=' ')
