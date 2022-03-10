N, K = map(int, input().split())
ans = N
for _ in range(K):
    if ans % 200 == 0:
        ans //= 200
    else:
        ans = ans * 1000 + 200
print(ans)
