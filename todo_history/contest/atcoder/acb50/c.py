N = int(input())


A = list(map(int, input().split()))

A = sorted(A)

if N % 2 == 0:
    for i in range(N):
        if A[i] != (i//2)*2 + 1:
            print(0)
            exit()
    print((2**(N//2)) % (10**9+7))

else:
    for i in range(N):
        if A[i] != ((i+1)//2)*2:
            print(0)
            exit()

    print((2**((N-1)//2)) % (10**9+7))
