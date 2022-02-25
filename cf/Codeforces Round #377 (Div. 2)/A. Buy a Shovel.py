P, R = map(int, input().split())
i = 1
while i * P % 10 != 0 and i * P % 10 != R: i += 1

print(i)
