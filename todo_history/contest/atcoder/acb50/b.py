N = int(input())
T = list(map(int, input().split()))
M = int(input())
t_sum = sum(T)

for i in range(M):
    t_idx, minus_t = map(int, input().split())
    print(t_sum - T[t_idx - 1] + minus_t)
