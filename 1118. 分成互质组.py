from math import gcd

#  TLE ...

N = 11
n, num_collection = int(input()), list(map(int, input().split()))
group, vt = [[0] * N for x in range(N)], [False] * N
ans = 10


def can_add_cur_group(cur_group_index, target_number, inner_end_index):
    for i in range(inner_end_index):
        if gcd(group[cur_group_index][i], target_number) > 1:
            return False
    return True


def depth_first_search(allcation_group_cnt, group_inner_add_index, search_start_index, added_cnt):
    global ans
    # 正确性 & basecase 剪枝
    if allcation_group_cnt >= ans:
        return
    # 组合型枚举
    if added_cnt == n:
        ans = min(allcation_group_cnt, ans)
        return
    need_allocate = True
    for i in range(search_start_index, n):
        if not vt[i] and can_add_cur_group(allcation_group_cnt, num_collection[i], group_inner_add_index):
            # 之所以把回溯逻辑加在这里，是因为在每个状态分支之间存在「独立状态」
            vt[i] = True
            # 覆盖式，不需要回溯
            group[allcation_group_cnt][group_inner_add_index] = num_collection[i]
            # 这里i + 1 的原因是， search_start_index 从0开始
            depth_first_search(allcation_group_cnt,
                               group_inner_add_index + 1, i + 1, added_cnt + 1)
            vt[i] = False
            need_allocate = False
    if need_allocate:
        depth_first_search(allcation_group_cnt + 1, 0, 0, added_cnt)


depth_first_search(1, 0, 0, 0)
print(ans)
