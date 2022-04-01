V, N = 30, 10000 + 10
f = [[0] * N for x in range(V)]
v, n = map(int, input().split())
w = [0] + list(map(int, input().split()))

def do ():
    f[0][0] = 1
    for i in range(1, v + 1):
        for j in range( n + 1):
            k = 0
            while k * w[i] <= j:
                f[i][j] += f[i - 1][j - k * w[i]]
                k += 1
    print(f[v][n])

do()