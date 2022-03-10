N = int(input())
s = list(map(int, input().split()))

s.sort()

cnt = 1
for i in range(1, len(s)):
    if s[i] != s[i - 1]: cnt += 1

print(cnt)
