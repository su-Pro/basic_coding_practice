N = int(input())
m = dict()
for _ in range(N):
    s, t = input().split()
    m.setdefault(s, int(t))

sorted_m = sorted(m.items(),key=lambda item:item[1])

print(sorted_m[-2][0])
