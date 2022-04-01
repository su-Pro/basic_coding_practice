a = list(map(int, input().split()))
cnt, prev = 0, 0
for v in a[:-1]:
    if v == 1:
        cnt += 1
        prev = 1
    else:
        if prev == 1 or prev == 0: prev = 0
        prev += 2
        cnt += prev
print(cnt)
