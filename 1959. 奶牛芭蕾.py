# def rotate_90(toP, fromP):
#     toP[0] -= fromP[0]
#     toP[1] -= fromP[1]
#     x, y = toP[1], - toP[0]
#     toP[0], toP[1] = x + fromP[0], y + fromP[1]

def rotate_90(a, b):
    b[0] -= a[0]
    b[1] -= a[1]
    x, y = b[1], -b[0]
    b[0], b[1] = a[0] + x, a[1] + y


p = [[0, 1], [1, 1], [0, 0], [1, 0]]
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
foot_ids = {"FL": 0, "FR": 1, "RL": 2, "RR": 3}  # 跟初始p的顺序保持一致。
op_ids = {"F": 0, "B": 2, "L": 3, "R": 1}  # 跟偏移量方向保持同步，才能实现动态朝向的移动

min_x, max_x, min_y, max_y = 0, 1, 0, 1
cur_direction = 0  # 初始化朝向东
for _ in range(int(input())):
    s = input()
    foot, op_ch = foot_ids[s[:2]], s[-1]
    if op_ch == 'P':
        # 其余三只脚进行旋转操作
        for _foot in range(4):
            if _foot != foot:
                rotate_90(p[foot], p[_foot])
        # 方向也要旋转90
        cur_direction = (cur_direction + 1) % 4
    else:
        # 做动态位移
        cur_direction = (cur_direction + op_ids[op_ch]) % 4
        p[foot][0] += dx[cur_direction]
        p[foot][1] += dy[cur_direction]
    # 检查是否存在“踩脚”
    for a in range(4):
        for b in range(a):
            if p[a] == p[b]:
                print('-1')
                exit(0)
    # 以四个蹄子的新坐标来更新四条边界
    for i in range(4):
        x, y = p[i]
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

print((max_x - min_x + 1) * (max_y - min_y + 1))
