n = int(input())


def getBase(base, n):

    def get(x):
        if x <= 9:
            return str(x)
        return chr((x - 10) + ord("A"))

    s = ''
    while n:
        s += get(n % base)
        n //= base
    return s[::-1]


def isOk(s):
    for l in range(len(s) // 2):
        if s[l] != s[len(s) - 1 - l]:
            return False
    return True


for i in range(1, 301):
    base_s = getBase(n, i * i)
    if isOk(base_s):
        print(getBase(n, i), base_s)
