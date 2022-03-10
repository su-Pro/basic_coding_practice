N, k = list(map(int, input().split()))

s = list(map(int, input().split()))
cnt = 0

left, right = k - 1, k

# mid => left
while left >= 0:
    if s[left] != 0: cnt += 1
    left -= 1

# mid => right
while right < len(s) and s[right - 1] == s[right] and s[right] != 0:
    cnt += 1
    right += 1

print(cnt)
