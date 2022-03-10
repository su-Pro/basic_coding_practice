"""
ID: supyyy21
LANG: PYTHON3
TASK: dualpal
"""

fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')

def writeAns(ans):
    fout.write(ans)
    fout.write('\n')

N, S = map(int, fin.readline().strip().split())

cnt, next_num = 0, S + 1  # 用来标记当前找了几个数字，停止循环


def getBase(base, next_num):
    sum = ""
    while next_num:
        # 注意顺序
        sum += str(next_num % base)
        next_num //= base
    return sum[::-1]


def check(t):
    for i in range(len(t) // 2):
        if t[i] != t[-i - 1]: return False
    return True


while cnt <= N - 1:
    is_twice = 0
    for i in range(2, 11):
        if check(getBase(i, next_num)): is_twice += 1
        if is_twice == 2:
            # 如果检查到两个元素后，我们认为这是一个有效的结果！
            writeAns(str(next_num))
            cnt += 1
            break
    # 接着往下检查
    next_num += 1

fout.close()
