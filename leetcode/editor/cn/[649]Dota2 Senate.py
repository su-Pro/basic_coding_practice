# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rDq = collections.deque(i for i,ch in enumerate(senate) if ch == "R")
        dDq = collections.deque(i for i, ch in enumerate(senate) if ch == "D")
        n = len(senate)
        while rDq and dDq:
            if rDq[0] < dDq[0]:
                dDq.popleft()
                rDq.append(rDq.popleft() + n)
            else:
                rDq.popleft()
                dDq.append(dDq.popleft() + n)
        return 'Radiant' if not dDq else 'Dire'
# leetcode submit region end(Prohibit modification and deletion)
