# ans = 20 * 60 + 10
s = list(map(int, input().split()))
cur_count = 20 * 60 + 10
total_count = 0

def dfs(pos, l_cnt, r_cnt):
    if pos >= len(a):
        global cur_count
        cur_count = min(cur_count, max(l_cnt, r_cnt))
        return cur_count
    dfs(pos + 1, l_cnt + a[pos], r_cnt)
    dfs(pos + 1, l_cnt, r_cnt + a[pos])


for _ in range(4):
    a = list(map(int, input().split()))
    cur_count = 20 * 60 + 10
    dfs(0, 0, 0)
    total_count += cur_count

print(total_count)