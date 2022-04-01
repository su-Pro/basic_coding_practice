from typing import List


class Solution(object):
    def maxSubArray(self, nums: List[int]):
        n = len(nums)
        dp = [0] + nums.copy()
        ans = float('-inf')
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1], 0) + nums[i - 1]
            ans = max(ans, dp[i])
        return ans
