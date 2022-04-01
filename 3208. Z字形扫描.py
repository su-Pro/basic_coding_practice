n = int(input())
g = [list(input().split()) for x in range(n)]
# True ↗ False ↙
direction = True
x, y = 0, 0
while x < n or y < n:
    if 0 <= x < n and 0 <= y < n:
        print(g[x][y], end=' ')
    if direction:
        x -= 1
        y += 1
    else:
        x += 1
        y -= 1
    # 处理两次边界反转
    if x < 0:
        x = 0
        direction = False
    if y < 0:
        y = 0
        direction = True
