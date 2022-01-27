# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dp, ret, cnt_zero, cnt_one = {}, 0, 0, 0
        dp[0] = 0
        for i in range(1, len(nums) + 1):
            current_v = nums[i - 1]
            if current_v == 0:
                cnt_zero += 1
            else:
                cnt_one += 1
            c = cnt_one - cnt_zero
            if c in dp:
                ret = max(ret, i - dp[c])
            else:
                dp[c] = i
        return ret
# leetcode submit region end(Prohibit modification and deletion)
