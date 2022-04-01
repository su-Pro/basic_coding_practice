n, a = int(input()), list(map(int, input().split()))
ans = 0
for i in range(1, n):
    ans = max(ans, abs(a[i] - a[i - 1]))
print(ans)
