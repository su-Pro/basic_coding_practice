N = int(input())
data = []
while len(data) < N * N:
    data.extend(list(map(int, input().split())))
a = [[0] * (N + 1)]
for i in range(N):
    a.append([0] + data[i * N: (i + 1) * N])


def smart():
    # 1. 按照列进行前缀和处理
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            a[i][j] += a[i - 1][j]
    ans = float('-inf')
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            # 把问题转化成1维
            f = 0
            for k in range(1, N + 1):
                w = a[j][k] - a[i - 1][k]
                f = max(f, 0) + w
                ans = max(ans, f)

    print(ans)


smart()


def simple():
    # 处理前缀和
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            a[i][j] += a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]

    ans = float('-inf')
    # S-TODO: 为什么这里的初始位置是从0开始？
    # 是为了能够计算一个最小的子矩阵吗？
    for x1 in range(0, N + 1):
        for y1 in range(0, N + 1):
            for x2 in range(x1 + 1, N + 1):
                for y2 in range(y1 + 1, N + 1):
                    ans = max(
                        ans,
                        a[x2][y2]
                        - a[x2][y1]
                        - a[x1][y2]
                        + a[x1][y1]
                    )

    print(ans)
