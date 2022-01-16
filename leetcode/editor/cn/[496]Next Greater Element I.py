# The next greater element of some element x in an array is the first greater 
# element that is to the right of x in the same array. 
# 
#  You are given two distinct 0-indexed integer arrays nums1 and nums2, where 
# nums1 is a subset of nums2. 
# 
#  For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[
# j] and determine the next greater element of nums2[j] in nums2. If there is no 
# next greater element, then the answer for this query is -1. 
# 
#  Return an array ans of length nums1.length such that ans[i] is the next 
# greater element as described above. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so 
# the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so 
# the answer is -1.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so 
# the answer is -1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length <= nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 10⁴ 
#  All integers in nums1 and nums2 are unique. 
#  All the integers of nums1 also appear in nums2. 
#  
# 
#  
# Follow up: Could you find an O(nums1.length + nums2.length) solution? Related 
# Topics 栈 数组 哈希表 单调栈 👍 626 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     ret = []
    #
    #     for n1 in nums1:
    #         l = nums2.index(n1)
    #         mv = n1
    #         for n2 in nums2[l:]:
    #             if n2 > mv:
    #                 mv = n2
    #                 break
    #         if mv == n1: ret.append(-1)
    #         else: ret.append(mv)
    #     return ret

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h_max = dict()
        ret = [-1] * len(nums1)
        stk = []

        for idx in range(len(nums2) - 1, -1, -1):
            val = nums2[idx]
            while stk and val >= stk[-1]: stk.pop()
            if not stk:
                h_max.setdefault(val, -1)
            else:
                h_max.setdefault(val, stk[-1])
            stk.append(val)
        for idx, n1 in enumerate(nums1):
            ret[idx] = h_max.get(n1)
        return ret
# leetcode submit region end(Prohibit modification and deletion)
