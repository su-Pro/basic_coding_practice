N, K = map(int, input().split())
ans = 0
low_sum = 0
for i in range(1, K + 1):
    low_sum += i

for i in range(1,N + 1):
    ans += i * 100 * K
    ans += low_sum


print(ans)