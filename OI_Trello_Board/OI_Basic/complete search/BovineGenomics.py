N, M = map(int, input().split())

a_cow = [input() for x in range(N)]  # 有斑点
b_cow = [input() for x in range(N)]

ant = 0

# 检查每一个位置:
for pos in range(M):
    used = False
    # 检查每头牛
    for a in range(N):
        for b in range(N):
            if a_cow[a][pos] == b_cow[b][pos]:
                used = True
                break

    if not used: ant += 1

print(ant)
