n = int(input())
a = [0]
for _ in range(n):
    a.append(int(input()))


def do():
    s = [0] + [0] * n
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]
    ant = 0
    for l in range(1, n + 1):
        for r in range(n, 0, -1):
            sumLR = s[r] - s[l - 1]
            if sumLR % 7 == 0:
                ant = max(ant, r - l + 1)
    return ant


print(do())
