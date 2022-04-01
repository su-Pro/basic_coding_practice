N, M = map(int, input().split())
g = [tuple(map(int, input().split())) for _ in range(N)]

l, r = 1, 1e5


def isOk(t):
    cnt = 0
    for w, h in g:
        cnt += (
            (w // t) * (h // t)
        )
    return cnt >= M


while l < r:
    m = l + r + 1 >> 1
    # isOk函数根据题意
    if(isOk(m)):
        l = m
    else:
        r = m - 1
# 此时的l就是最终答案
print(l)
# 逻辑是对的，但是超时了...
