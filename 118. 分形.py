from cgi import print_arguments
from operator import le


N = pow(3, 8)
g = [[False] * N for _ in range(N)]


p_double_x, p_double_y = (0, 1, 2, 2), (2, 1, 0, 2)


def dfs(level):
    if level == 1:
        g[0][0] = True
        return
    dfs(level - 1)
    # copy to four square
    w_square = 1
    for i in range(level - 2):
        w_square *= 3

    for p in range(4):
        for i in range(w_square):
            for j in range(w_square):
                g[p_double_x[p] * w_square + i][p_double_y[p]
                                                * w_square + j] = g[i][j]


dfs(7)

# python 答案正确，但是超时...
while True:
    n = int(input())
    if n == -1:
        break
    # 输出每次询问,输出一个 w = 3 ^ n - 1
    w_square = pow(3, n - 1)
    for i in range(w_square):
        l = ''
        for j in range(w_square):
            if g[i][j]:
                l += 'X'
            else:
                l += ' '
        print(l)
    print('-')
