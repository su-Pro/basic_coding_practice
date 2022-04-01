N = int(1e4) + 10
n, m = map(int, input().split())


def smart_interval():
    intervals = []
    for _ in range(m):
        intervals.append(tuple(map(int, input().split())))
    intervals.sort(key=lambda i: i[0])

    l, r = intervals[0]
    m_intervals = []  # 对区间进行合并
    for i in range(1, m):
        nl, nr = intervals[i]
        if nl <= r:
            # merge
            r = max(r, nr)
        else:
            m_intervals.append((l, r))
            l, r = nl, nr
    m_intervals.append((l, r))  # 不要漏掉最后一个区间
    cnt = n + 1
    for l, r in m_intervals:
        cnt -= r - l + 1
    print(cnt)


def brute():
    N = int(1e4) + 10
    n, m = map(int, input().split())
    vs = [False] * N

    for i in range(n + 1):
        vs[i] = True

    for _ in range(m):
        l, r = map(int, input().split())
        for i in range(l, r + 1):
            vs[i] = False

    print(vs.count(True))


smart_interval()
