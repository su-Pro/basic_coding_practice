s = list(map(int, input().split()))

s.sort()

if s[1] - s[0] == s[2] - s[1]:
    print("Yes")
else:
    print("No")

