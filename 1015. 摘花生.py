N = 110

def do():
    n, m = list(map(int, input().split()))
    w, f = [[0] * N for x in range(N)], [[0] * N for x in range(N)]
    for i in range(1, n + 1):
        w[i] = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 通过初始化足够大的矩阵，避免边界处理
            f[i][j] = max(f[i - 1][j], f[i][j - 1]) + w[i][j]
    return f[n][m]


for _ in range(int(input())):
    print(do())
