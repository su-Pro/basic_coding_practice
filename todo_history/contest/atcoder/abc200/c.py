N = int(input())

a = list(map(int, input().split()))

def solve (a,b):
    ans = a - b
    return ans % 200 == 0


cnt = 0

for i in range(N):
    for j in range(i + 1,N):
        if solve(a[i],a[j]): cnt += 1

print(cnt)