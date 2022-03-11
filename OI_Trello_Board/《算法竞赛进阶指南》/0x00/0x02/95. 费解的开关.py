from copy import deepcopy

N = 5
n = int(input())


def turn(board, row, col):
    dx, dy = (0, 1, 0, -1, 0), (1, 0, -1, 0, 0)
    # 遍历四个方向进行取反操作,不要忘了自己也会操作一次
    for i in range(5):
        nx, ny = row + dx[i], col + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] = '0' if board[nx][ny] == '1' else '1'


def doWork(board):
    minAns = float('inf')
    # 按照每一位可能的操作进行遍历解空间
    for p in range(1 << N):
        count = 0
        bCopy = deepcopy(board)
        # 统计在这种case下，需要按的次数：
        for col in range(N):
            # 检查是否需要按，从低位依次检查到高位
            if p >> col & 1:
                count += 1
                turn(bCopy, 0, col)

        # 按照性质开始递推工作
        for r in range(N - 1):
            for c in range(N):
                if bCopy[r][c] == '0':
                    count += 1
                    turn(bCopy, r + 1, c)

        # 查看最后一行的状态，只要有一个还亮，则说明不满足情况
        # 如何像js那种函数式写法呢？
        allLight = True
        for s in bCopy[-1]:
            if s == '0':
                allLight = False
                break

        if allLight: minAns = min(minAns, count)

    return -1 if minAns > 6 else minAns


# 处理每一个询问
for _ in range(n):
    board = [
        list(input()) for i in range(N)
    ]
    if _ != n - 1: input()
    print(doWork(board))
