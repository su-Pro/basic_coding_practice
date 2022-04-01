n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 0
mid_value = n // 2

for v in a:
    ans += abs(v - a[mid_value])

print(ans)
