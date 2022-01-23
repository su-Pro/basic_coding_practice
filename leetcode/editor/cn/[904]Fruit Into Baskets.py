# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ret = 0
        l = 0
        basketDict = dict()

        for r,type in enumerate(fruits):
            if type not in basketDict:
                basketDict.setdefault(type, 1)
            else:
                basketDict[type] += 1
            while len(basketDict) > 2:
                basketDict[fruits[l]] -= 1
                if basketDict[fruits[l]] == 0:
                    del basketDict[fruits[l]]
                l += 1
            ret = max(ret, r - l + 1)
        return ret
# leetcode submit region end(Prohibit modification and deletion)

s = Solution().totalFruit([1,2,3,2,2])