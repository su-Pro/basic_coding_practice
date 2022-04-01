S = input()

start, end = [-1] * 26, [-1] * 26

# fill idx
for i, ch in enumerate(S):
    # 说明还没入场，应该加入到start组中
    if start[ord(ch) - ord("A")] == -1:
        start[ord(ch) - ord("A")] = i
    else:
        end[ord(ch) - ord("A")] = i
ans = 0
# 检查 AB 元素之间的关系是否满足： start i < start j < end i < end j
for a in range(26):
    for b in range(26):
        ans += (start[a] < start[b] < end[a] < end[b])

print(ans)
