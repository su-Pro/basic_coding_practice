# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n
        stk = []

        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                cur_idx = stk.pop()
                ret[cur_idx] = i - cur_idx
            stk.append(i)

        return ret
s = Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
# leetcode submit region end(Prohibit modification and deletion)
