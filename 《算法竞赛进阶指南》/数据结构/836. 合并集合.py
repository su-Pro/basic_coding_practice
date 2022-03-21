N, M = map(int, input().split())
fa = [0] * (N + 1)


def makeSet(size):
    global fa
    for i in range(1, N + 1):
        fa[i] = i


def merge(a, b):
    global fa
    rotA, rotB = find(a), find(b)
    fa[rotA] = rotB


def find(a):
    global fa
    if fa[a] != a:
        fa[a] = find(fa[a])
    return fa[a]


makeSet(N)

for _ in range(M):
    opt, a, b = list(input().split())
    a, b = int(a), int(b)
    if opt == 'M':
        if find(a) == find(b):
            continue
        merge(a, b)
        continue
    print(
        'Yes' if find(a) == find(b) else 'No'
    )
