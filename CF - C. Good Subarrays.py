t = int(input())


def do(n, a):
    s = [0] + [0] * n
    a = [0] + a
    cnt = 0
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]

    for l in range(1, n + 1):
        for r in range(l, n + 1):
            sumLR = s[r] - s[l - 1]
            if sumLR != (r - l) + 1: continue
            cnt += 1
    return cnt


for _ in range(t):
    n, a = int(input()), list(map(int, list(input())))
    print(do(n, a))
