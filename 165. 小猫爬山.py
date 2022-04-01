n, w = map(int, input().split())
cab = [0] * (n + 1)
c = [0] * (n + 1)
# 读入重量
for i in range(1,n + 1):
    c[i] = int(input())
ans = n


def dfs(now, cnt):
    global ans
    if cnt > ans: return
    if now == n + 1:
        ans = min(ans, cnt)
        return
    # 能加入其中一个缆车
    for i in range(1, cnt + 1):
        if cab[i] + c[now] <= w:
            cab[i] += c[now]
            dfs(now + 1, cnt)
            cab[i] -= c[now]
    # 新开缆车,更新重量
    cab[cnt + 1] = c[now]
    dfs(now + 1, cnt + 1)
    cab[cnt + 1] = 0


dfs(1, 0)
print(ans)
