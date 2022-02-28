# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        cur_seg, ans = [-float('inf'), -float('inf')], []

        for seg_st, seg_ed in intervals:
            # 说明一定没有相交区间了...
            if seg_st > cur_seg[1]:
                ans.append(cur_seg)
                cur_seg = [seg_st, seg_ed]
            # 要合并
            else:
                # case1: 包含 & case2: 相交
                cur_seg[1] = max(cur_seg[1], seg_ed)
        # 最后还有一个孤独的区间... 也要加入到结果集中！
        ans.append(cur_seg)
        return ans[1:]


# leetcode submit region end(Prohibit modification and deletion)
