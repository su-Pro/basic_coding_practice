# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMinArrowShots(self, seg: List[List[int]]) -> int:
        seg = sorted(seg, key=lambda v: v[0])
        l, r, ans = seg[0][0], seg[0][1], 1

        # ans 之所以设置为1，是因为还没有开始合并区间之前，就已经存在一个区间在等待被射。
        # 和经典的合并区间差异在于，我们合并策略是产生最小的区间，而不是逐渐变大。

        for i in range(1, len(seg)):
            cur_seg = seg[i]
            if cur_seg[0] <= r:
                r = min(r, cur_seg[1])
            else:
                ans += 1
                l, r = cur_seg

        return ans
# leetcode submit region end(Prohibit modification and deletion)
