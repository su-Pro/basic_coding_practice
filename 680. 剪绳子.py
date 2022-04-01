n, m = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, max(a)


def check(target_len):
    cnt = 0
    for v in a:
        cnt += v // target_len
    # TODO: 注意这里的逻辑，是 >= 而不是 ==
    return cnt >= m


while r - l >= 1e-4:
    mid = (l + r) / 2
    if check(mid):
        l = mid
    else:
        r = mid

print('%.2f' % l)
