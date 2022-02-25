"""
ID: supyyy21
LANG: PYTHON3
TASK: transform
"""

fin = open('transform.in', 'r')
fout = open('transform.out', 'w')

import copy

N = int(int(fin.readline().strip()))
a, b = [list(fin.readline().strip()) for i in range(N)], \
       [list(fin.readline().strip()) for i in range(N)]


def mirror(temp):
    for i in range(N):
        l, r = 0, N - 1
        while l < r:
            temp[i][l], temp[i][r] = temp[i][r], temp[i][l]
            l += 1
            r -= 1
    return temp


# 对角线翻转
def rote_right_angle(temp):
    for i in range(N):
        for j in range(0, i):
            temp[i][j], temp[j][i] = temp[j][i], temp[i][j]
    return mirror(temp)


def check(a, target):
    temp = copy.deepcopy(a)
    # 先rote 90，180，270
    for i in range(1, 4):
        if rote_right_angle(temp) == target: return i
    # 再镜像一下
    temp = copy.deepcopy(a)
    if mirror(temp) == target: return 4
    # 还不行，就开始组合 rote 90，180，270
    for i in range(3):
        if rote_right_angle(temp) == target: return 5
    # 判断是否最开始的就是和目标相同啊？
    if a == target: return 6
    return 7


fout.write(str(check(a, b)))
fout.write('\n')
fout.close()
