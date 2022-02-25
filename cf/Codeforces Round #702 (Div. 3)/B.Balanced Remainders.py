def doit():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0, 0, 0]
    for x in a:
        b[x % 3] += 1
    ans = 0
    while True:
        u = False
        for i, x in enumerate(b):
            # 如何证明这里，反条件就是 x == n // 3???
            if (x > n // 3):
                u = True
                ans += x - n // 3
                b[(i + 1) % 3] += x - n // 3
                b[i] = n // 3
        if (not u): break
    print(ans)


T = int(input())
for _ in range(T):
    doit()