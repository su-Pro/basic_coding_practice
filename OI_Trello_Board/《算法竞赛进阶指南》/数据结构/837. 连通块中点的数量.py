N, t = map(int, input().split())


def makSet(size):
    fa = [0] * size
    for i in range(size): fa[i] = i


def find(x):
    if x != fa[x]: fa[x] = find(fa[x])
    return fa[x]


def merge(a, b):
    rA, rB = find(a), find(b)
    sn[rB] += sn[rA]  # 更新大小
    fa[rA] = rB  # 把a的祖先，移到b祖先下面


fa, sn = makSet(N + 1), [1] * (N + 1)
for _ in range(t):
    l = list(input().split())
    idy = l[0]
    if idy == 'C':
        a, b = map(int, l[1:])
        if find(a) == find(b): continue
        merge(a, b)
    elif idy == 'Q1':
        a, b = map(int, l[1:])
        print('Yes' if find(a) == find(b) else "No")
    else:
        print(sn[find(int(l[1]))])
