n, a = int(input()), list(map(int, input().split()))
cnt = 0
for l in range(n - 2):
    r = l + 2
    if a[l] > a[l + 1] < a[r] or a[l] < a[l + 1] > a[r]: cnt += 1

print(cnt)
