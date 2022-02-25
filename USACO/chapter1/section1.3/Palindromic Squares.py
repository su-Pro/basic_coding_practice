"""
ID: supyyy21
LANG: PYTHON3
TASK: palsquare
"""

fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')


def writeAns(ans):
    fout.write(ans)
    fout.write('\n')


N = int(fin.readline().strip())


def get(x):
    if x <= 9: return str(x)
    return chr((x - 10) + ord("A"))


def getBaseN(i, base):
    s = ""
    while i:
        s += get(i % base)
        i //= base
    s = s[::-1]
    return s


def check(baseNstr):
    for l in range(len(baseNstr) // 2):
        if baseNstr[l] != baseNstr[len(baseNstr) - 1 - l]: return False
    return True


for i in range(1, 301):
    baseNstr = getBaseN(i * i, N)
    if not check(baseNstr): continue

    writeAns(getBaseN(i, N) + " " + baseNstr)

fout.close()
