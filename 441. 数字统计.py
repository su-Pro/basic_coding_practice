l, r = map(int, input().split())
cnt = 0
for v in range(l, r + 1):
    j = v
    while j:
        if j % 10 == 2: cnt += 1
        j //= 10
print(cnt)
