N = int(input())

for _ in range(N):
    s = ""
    n, a, b = list(map(int, input().split()))
    for i in range(n):
        s += chr(ord('a') + (i % b))
    print(s)
