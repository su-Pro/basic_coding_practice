n = int(input())

s = []
for _ in range(n):
    s.append([_ + 1] + list(map(int, input().split())))

# 1. 按照总数排序
s.sort(key=lambda _s: sum(_s[1:]))
# 2. 按照语文顺序排序
s = s.sort(key=lambda _s: _s[1])
# 3. 按照学号排序
s.sort(key=lambda _s: _s[0])
for i in range(5):
    print(s[0], sum(s[1:]))
