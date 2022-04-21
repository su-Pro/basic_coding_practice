def ipt(): return map(int, input().split())


N = int(1e6 + 5)

n, q = ipt()
a = list(ipt())

for _ in range(q):
    t = int(input())
    l, r = 0, len(a) - 1
    while l < r:
        mid = l + r >> 1
        if a[mid] >= t:
            r = mid
        else:
            l = mid + 1
    if a[l] != t:
        print(-1, -1)
        continue
    else:
        # 搜索右边
        print(l, end=' ')
        l, r = 0, len(a) - 1
        while l < r:
            mid = l + r + 1 >> 1
            if a[mid] <= t:
                l = mid
            else:
                r = mid - 1
        print(l)
