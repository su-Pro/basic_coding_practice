from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i - 1]: continue
            l, r = i - 1, i + 1
            while l > 0 and nums[l] == nums[i]: l -= 1
            while r < len(nums) - 1 and nums[r] == nums[i]: r += 1
            if nums[l] < nums[i] and nums[r] < nums[i]:
                cnt += 1
                continue
            if nums[l] > nums[i] and nums[r] > nums[i]: cnt += 1
        return cnt
# Solution().countHillValley([2,4,1,1,6,5])