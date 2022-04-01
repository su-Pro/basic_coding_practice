# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_len = len(nums) + 1
        dp = [0] * prefix_len

        # init prefix dp
        for i in range(1, prefix_len):
            dp[i] = dp[i - 1] + nums[i - 1]

        dict = {}
        for i in range(2, prefix_len):
            dict.setdefault(dp[i - 2] % k)
            if dp[i] % k in dict: return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
