N = int(1e3) * int(1e3) + 5
ipt = lambda: map(int, input().split())
n, m = ipt()

current_a, current_b = [0] * N, [0] * N  # 同一时间，分别走到哪里

current = 0
for _ in range(n):
    v, t = ipt()
    while t:
        t -= 1
        current += 1
        current_a[current] += current_a[current - 1] + v

current = 0
for _ in range(m):
    v, t = ipt()
    while t:
        t -= 1
        current += 1
        current_b[current] += current_b[current - 1] + v

# 检查同一时间段a 和 b 的距离差
ans = 0
curNo = ''
for t in range(1, current + 1):
    if current_a[t] > current_b[t]:
        if curNo == 'b': ans += 1
        curNo = 'a'
    elif current_b[t] > current_a[t]:
        if curNo == 'a': ans += 1
        curNo = 'b'

print(ans)
