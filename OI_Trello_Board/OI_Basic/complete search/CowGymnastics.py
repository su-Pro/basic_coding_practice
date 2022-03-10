# import sys
#
# sys.stdin = open("gymnastics.in", "r")
# sys.stdout = open("gymnastics.out", "w")

K, N = map(int, input().split())

s = [
    list(map(int, input().split())) for x in range(K)
]

cnt = 0


def getBetter(x, y, s_n):
    pos_x, pos_y = 0, 0
    for idx, v in enumerate(s[s_n]):
        if v == x: pos_x = idx
        if v == y: pos_y = idx

    return pos_x > pos_y


def getBetterN(x, y):
    cnt = 0
    for s_n in range(K):
        if getBetter(x, y, s_n): cnt += 1
    return cnt


for x in range(1,N + 1):
    for y in range(1,N + 1):
        if getBetterN(x, y) == K:
            cnt += 1

print(cnt)
