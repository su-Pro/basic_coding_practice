import collections
from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        ret = []
        for v in nums:
            if d[v] == 1 and v - 1 not in d and v + 1 not in d:
                ret.append(v)
        return ret
