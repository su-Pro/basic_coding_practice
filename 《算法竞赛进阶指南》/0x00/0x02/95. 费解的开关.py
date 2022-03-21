import copy

X = 5
N = int(input())


def turn(b, i, j):
    x, y = (0, 0, 1, 0, -1), (0, 1, 0, -1, 0)
    for d in range(5):
        nx, ny = i + x[d], j + y[d]
        if 0 <= nx < X and 0 <= ny < X:
            b[nx][ny] = '0' if b[nx][ny] == '1' else '1'


def doWork(board):
    ans = float('inf')
    for p in range(1 << X):
        b = copy.deepcopy(board)
        cnt = 0
        for col in range(X):
            if 1 & p >> col:
                cnt += 1
                turn(b, 0, col)

        for row in range(X - 1):
            for col in range(X):
                if b[row][col] == '0':
                    cnt += 1
                    turn(b, row + 1, col)
        canUpdate = True
        for v in b[-1]:
            if v == '0':
                canUpdate = False
                break

        if canUpdate: ans = min(ans, cnt)

    return -1 if ans > 6 else ans


for i in range(N):
    board = [list(input()) for _ in range(X)]
    if i != N - 1: input()
    print(doWork(board))
