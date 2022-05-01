# from typing import List
#
#
# class Solution:
#     def minimumCardPickup(self, cards: List[int]) -> int:
#         n = len(cards)
#         ans = float('inf')
#         for l in range(n - 1):
#             cur_set = set()
#             cur_set.add(cards[l])
#             for r in range(l + 1, n):
#                 if cards[r] in cur_set:
#                     ans = min(ans, r - l + 1)
#                 else:
#                     cur_set.add(cards[l])
#         return -1 if ans == float('inf') else ans
import collections
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        m = collections.defaultdict(list)
        for idx, ch in enumerate(cards):
            m[ch].append(idx)

        ans = float('inf')
        for ch in tuple(set(m)):
            if len(m[ch]) <= 1:
                continue
            # m[ch] 中的元素都是从小到大排序，但不保证一定是长度最短的！
            for i in range(len(m[ch]) - 1):
                ans = min(ans, m[ch][i + 1] - m[ch][i] + 1)

        return -1 if ans == float('inf') else ans