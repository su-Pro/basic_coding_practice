# import sys
#
# sys.stdin = open("paint.in", "r")
# sys.stdout = open("paint.out", "w")

N = int(input())
f = list(map(int, input().split()))
ans = 0
# 枚举到所有照片
for a in range(N):
    for b in range(a, N):
        average = sum(f[a: b + 1]) / len(f[a: b + 1])
        # 检查是否作为最终结果: 照片中的画，其中有一个的花瓣数等于平均数
        for f_count in f[a:b + 1]:
            if f_count == average:
                ans += 1
                break

print(ans)
