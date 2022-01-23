from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a, b = [], []  # a < 0 b > 0
        ret = []

        for v in nums:
            if v < 0:
                a.append(v)
            else:
                b.append(v)

        for i in range(len(nums) // 2):
            ret.append(b[i])
            ret.append(a[i])
        return ret
