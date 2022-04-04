import collections
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, los_set, los = set(), set(), []
        for x in matches:
            win.add(x[0])
            los_set.add(x[1])
            los.append(x[1])

        ans_a = [x for x in win if x not in los_set]
        _b = collections.Counter(los)
        ans_b = [x for x in _b if _b[x] == 1]
        ans_a.sort()
        ans_b.sort()
        return ans_a, ans_b
