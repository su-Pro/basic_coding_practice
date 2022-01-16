# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        for i in range(n):
            piles[i] = - piles[i]

        heapq.heapify(piles)

        for i in range(k):
            top = heapq.heappop(piles)
            heapq.heappush(piles,top + ((-top) // 2))

        return - sum(piles)
# leetcode submit region end(Prohibit modification and deletion)
