import heapq

N = int(input())
S = []
needSort = False


def queryGreater(t, nth):
    # 1. 找到最接近t的一个索引 x 左侧
    l, r = 0, len(S) - 1
    while l < r - 1:
        m = (l + r) // 2
        if S[m] > t:
            r = m
        else:
            l = m
    x = r if S[r] == t else l
    if x + nth < len(S):
        return S[x + nth]
    else:
        return -1
    # 2. 如果nth + x 越界，则返回 -1


def queueLess(t, nth):
    # 1. 找到最接近t的一个索引 x 左侧
    l, r = 0, len(S) - 1
    while l < r - 1:
        m = (l + r) // 2
        if S[m] > t:
            r = m
        else:
            l = m
    x = l if S[l] == t else r
    if x - nth >= -1:
        return S[x - nth + 1]
    else:
        return -1
    # 2. 如果nth + x 越界，则返回 -1


for _ in range(N):
    Q = tuple(map(int, input().split()))
    if Q[0] == 1:
        S.append(Q[1])
        needSort = True
    elif Q[0] == 2:
        if needSort:
            S.sort()
        print(queueLess(Q[1], Q[2]))
        needSort = False
else:
    if needSort:
        S.sort()
    print(queryGreater(Q[1], Q[2]))
    needSort = False
