S = input()
ans = 0
for i in range(10000):
    # 这里到底是用来做什么的？为什么下面检查的时候要检查那么多次？？？？
    flag = [False] * 10
    now = i
    # 四个位置
    for _ in range(4):
        flag[now % 10] = True
        now //= 10
    flag2 = True
    # 检查当前这一位
    for i, ch in enumerate(S):
        if ch == 'o' and not flag[i]:
            flag2 = False
        if ch == 'x' and flag[i]:
            flag2 = False
    ans += flag2
print(ans)
