N = int(input())
# 如何让每个值 - 1呢？
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

pre_count = [0] * (N + 1)
for i in range(N):
    pre_count[B[C[i] - 1] - 1] += 1

ans = 0
for i in range(N):
    # 所有case的集合
    ans += pre_count[A[i] - 1]
print(ans)
