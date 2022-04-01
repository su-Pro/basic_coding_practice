N, P, H, M = map(int, input().split())


def brute():
    ans = [0] * N

    for _ in range(M):
        a, b = map(lambda v: int(v) - 1, input().split())
        if a > b:
            a, b = b, a
        for i in range(a + 1, b):
            ans[i] -= 1

    ans = list(map(lambda v: v + H, ans))

    print(ans)


def prefix():
    s = [0] * (N + 1)
    c = [0] * (N + 1)
    # 处理端点
    vs = set()
    for _ in range(M):
        a, b = map(lambda v: int(v), input().split())
        if a > b: a, b = b, a
        # 去重复
        if (a, b) in vs: continue
        # 端点处理
        s[a + 1] -= 1
        s[b] += 1
        vs.add((a, b))

    # 求相对值（不太理解这里和前缀和有毛关系？）
    for i in range(1, N + 1):
        # 这里为什么是对c[i]进行操作呢？
        c[i] = c[i - 1] + s[i]
        print(c[i] + H)


prefix()
