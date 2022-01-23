from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0

        for v in nums:
            if nums[0] < v < nums[-1]: cnt += 1

        return cnt
