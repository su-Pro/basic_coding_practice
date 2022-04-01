t, pos, cur = int(input().split()[1]), list(map(int, input().split())), 1

while cur < t: cur += pos[cur - 1]
print("YES" if cur == t else "NO")


def dfs(h):
    if h == t:
        return True
    if h > t:
        return False
    return dfs(h + pos[h - 1])
