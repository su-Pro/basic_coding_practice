from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        max_s, ans = 0, []
        for i in range(1 << len(aliceArrows)):
            kb, cur_count, cur_score = [0] * 12, 0, 0
            for area, ka in enumerate(aliceArrows):
                # 代表我们枚举的这种情况，要在area这个面积上，打赢A同学
                if i >> area & 1:
                    cur_score += area
                    cur_count += ka + 1
                    kb[area] = ka + 1
            # bade case
            if cur_count > numArrows: continue
            # 正确答案的同时，记得更新kb[0] （虽然对最终结果没有任何影响）
            kb[0] = numArrows - cur_count
            # 打擂台，更新结果
            if cur_score > max_s:
                max_s = cur_score
                ans = kb.copy()
        return ans
