from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        min_c = min(candies)
        def isOk(m):
            _k = 0
            for c in candies:
                _k += c // m
            a = m * _k
            return a <= total and _k >= k

        total = sum(candies)
        l, r = 0, total
        while l < r:
            m = l + r + 1 >> 1
            # isOk函数根据题意
            if (isOk(m)):
                l = m
            else:
                r = m - 1
        return l

#  3
Solution().maximumCandies(
[1,2,3,4,10],
5
)
