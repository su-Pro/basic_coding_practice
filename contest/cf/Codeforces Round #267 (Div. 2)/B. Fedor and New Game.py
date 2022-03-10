n, m, k = list(map(int, input().split()))

friends = [int(input()) for i in range(m + 1)]

cnt = 0
for f in friends[:-1]:
    if bin(f ^ friends[-1]).count('1') <= k:
        cnt += 1

print(cnt)
