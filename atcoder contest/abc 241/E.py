N, K = map(int, input().split())
A = list(map(int, input().split()))
X = 0

for _ in range(K):
    pos = X % N
    X += A[pos]
    print('run')

print(X)
