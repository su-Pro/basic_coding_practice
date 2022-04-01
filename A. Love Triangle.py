n, p = int(input()), list(map(lambda v: int(v) - 1, input().split()))


def smartWalker():
    for i in range(n):
        cnt = 3
        pos = i
        while cnt:
            pos = p[pos]
            cnt -= 1
        if pos == i:
            return print('YES')
    print('NO')


def short():
    # 三角关系,三步位移
    return 'YES' if [i for i in range(n) if p[p[p[i]]] == i] else 'NO'


smartWalker()

print(short())