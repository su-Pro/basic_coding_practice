N = 7
anger_level = 0
day = -1
for i in range(1, N + 1):
    u, v = map(int, input().split())
    if u + v > 8 and u + v > anger_level:
        anger_level = u + v
        day = i

if day == -1: print(0)
else:
    print(day)
