dx, dy, curD = [1, 0, -1, 0], [0, -1, 0, 1], 0

N = int(input())
S = list(input())
x,y = 0,0
for c in S:
    if c == 'R':
        curD = (curD + 1) % 4
    else:
        x += dx[curD]
        y += dy[curD]
print(x,y)
