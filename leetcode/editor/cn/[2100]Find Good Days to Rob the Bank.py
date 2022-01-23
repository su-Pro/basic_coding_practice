# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], t: int) -> List[int]:
        n = len(security)
        o1, o2 = 0, 0
        if t == 0:
            return [i for i in range(0, n)]
        if t * 2 + 1 > n:
            return []
        ret = []
        for i in range(1, t + 1):
            if security[i] > security[i - 1]: o1 += 1

        for i in range(t + 1, t * 2 + 1):
            if security[i] < security[i - 1]: o2 += 1

        l, r = 0, t * 2
        for p in range(t, n - t):
            if o1 is 0 and o2 is 0: ret.append(p)
            if r + 1 is n: break
            if security[l] < security[l + 1]: o1 -= 1  # 说明左边少了一个"不可能正确的值"
            if security[p] < security[p + 1]: o1 += 1  # 又多了一个"不可能正确的值"
            if security[p] > security[p + 1]: o2 -= 1
            if security[r + 1] < security[r]: o2 += 1

            l += 1
            r += 1

        return ret
# leetcode submit region end(Prohibit modification and deletion)

s = Solution().goodDaysToRobBank([1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8],2)