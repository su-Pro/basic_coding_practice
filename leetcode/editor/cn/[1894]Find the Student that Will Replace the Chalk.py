# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # 利用求模运算来去掉不必要的遍历
        remain_k,ans = k % sum(chalk),0
        for i,v in enumerate(chalk):
            if remain_k < v:
                ans = i
                break
            remain_k -= v
        return ans
# leetcode submit region end(Prohibit modification and deletion)
