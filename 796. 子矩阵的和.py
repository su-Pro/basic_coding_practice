n, m, q = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

def twoDprefixSum(a):
    s = [[0] * (m + 1) for x in range(n + 1)]  # 注意左和上边都要补一个0，方便计算
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] + a[i - 1][j - 1] - s[i - 1][j - 1]
    return s

s = twoDprefixSum(a)
for _q in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(
        s[x2][y2]
        - s[x1 - 1][y2]
        - s[x2][y1 - 1]
        + s[x1 - 1][y1 - 1]
    )
