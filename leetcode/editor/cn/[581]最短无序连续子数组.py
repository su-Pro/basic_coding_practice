# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = len(nums)

        if l == 1: return 0

        up_stk = [(nums[0], 0)]
        down_stk = [(nums[-1], l - 1)]

        break_up, break_down = l, 0

        for i in range(1, l):
            while up_stk and nums[i] < up_stk[-1][0]:
                break_up = min(break_up, up_stk.pop()[1])
            up_stk.append((nums[i], i))

        for i in range(l - 2, -1, -1):
            while down_stk and nums[i] > down_stk[-1][0]:
                break_down = max(break_down,down_stk.pop()[1])
            down_stk.append((nums[i], i))
        distance = break_down - break_up + 1
        return 0 if distance < 0 else distance


# leetcode submit region end(Prohibit modification and deletion)

s = Solution().findUnsortedSubarray([1, 2, 4, 5, 6])

# [1,3,2,2,2]
