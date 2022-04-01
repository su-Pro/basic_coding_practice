N, A = int(input()), list(map(int, input().split()))


# 需要对整个搜索路径进行求和，保证在叶节点能轻松比较
def solve(level, leftPath, rightPath):
    # 已经到了叶子节点,换句话说，已经没有能再选择的苹果了
    # 进行battle
    if level == N:
        return abs(leftPath - rightPath)

    # 两层状态往下走
    left = solve(level + 1, leftPath + A[level], rightPath)
    right = solve(level + 1, leftPath, rightPath + A[level])
    return min(left, right)


def bitmasks():
    ans = float('inf')
    # 枚举所有可能的二进制串儿
    for mask in range(1 << N):
        l, r = 0, 0
        # 一共检查N次，因为只有N个数
        for i in range(N):
            # 从右向左检查当前串儿是否是1(代表左集合要这个值)
            if mask & (1 << i):
                l += i
            else:
                r += i
        ans = min(ans, abs(l - r))


print(solve(0, 0, 0))
