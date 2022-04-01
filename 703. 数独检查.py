T = int(input())


def x_y_ok(direction):
    flag = True
    for x in range(n * n):
        vs = [False] * (n * n + 1)
        for y in range(n * n):
            v = g[x][y] if direction == 'x' else g[y][x]
            if v < 1 or v > n * n or vs[v]:
                return False
            vs[v] = True
    return flag


def square_ok():
    for i in range(n):
        for j in range(n):
            # 找到每个顶点
            for x in range(n):
                for y in range(n):
                    vs = [False] * (n * n + 1)
                    v = g[i + x][j + y]
                    if v < 1 or v > n * n or vs[v]:
                        return False
                    vs[v] = True
    return True


for _ in range(T):
    n = int(input())
    g = [list(map(int, input().split())) for x in range(n * n)]
    # TODO: ** 是什么？
    if x_y_ok('x') and x_y_ok('y') and square_ok():
        print(True)
    else:
        print(False)
