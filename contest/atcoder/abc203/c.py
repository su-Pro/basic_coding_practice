N, K = map(int, input().split())
friends_award = dict()
# 统计能给钱的不同朋友总金额
for _ in range(N):
    f, w = map(int, input().split())
    if f not in friends_award:
        friends_award[f] = 0
    friends_award[f] += w

# 起初能到达的目的地
d = K

# 这里一定要排序才能保证正确性
for s, v in sorted(friends_award.items(), key=lambda f: f[0]):
    if d >= s:
        d += v
    else:
        break

print(d)
