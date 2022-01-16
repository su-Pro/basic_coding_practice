# Given an integer array nums, return true if there exists a triple of indices (
# i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such 
# indices exists, return false. 

#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 
# 4 < nums[5] == 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5 * 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you implement a solution that runs in O(n) time complexity 
# and O(1) space complexity? Related Topics 贪心 数组 👍 452 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = len(nums)
        l_min = [0] * l
        r_max = [0] * l
        l_min[0] = nums[0]
        r_max[l - 1] = nums[l - 1]
        # fill min value ,from left to right
        for i in range(1, l):
            l_min[i] = min(l_min[i - 1], nums[i])

        for i in range(l - 2, -1, -1):
            r_max[i] = max(r_max[i + 1], nums[i])

        for i in range(1, l - 1):
            if l_min[i - 1] < nums[i] < r_max[i + 1]: return True
        return False


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
s.increasingTriplet([2, 1, 5, 0, 4, 6])
