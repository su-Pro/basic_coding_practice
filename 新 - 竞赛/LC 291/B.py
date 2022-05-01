from typing import List
import collections


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        solution = [
            ed - st + 1 for st in range(n) for ed in range(st + 1, n) if cards[st] == cards[ed]]
        return -1 if not solution else min(solution)


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        soultion, memo_st = [], {}
        for ed, x in enumerate(cards):
            if x in memo_st:
                soultion.append(ed - memo_st[x] + 1)
            memo_st[x] = ed
        return -1 if not soultion else min(soultion)


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        D = float('inf')
        m = collections.defaultdict(list)
        for idx, ch in enumerate(cards):
            m[ch].append(idx)

        ans = D
        for ch in tuple(set(m)):
            if len(m[ch]) <= 1:
                continue
            for i in range(len(m[ch]) - 1):
                ans = min(ans, m[ch][i + 1] - m[ch][i] + 1)

        return -1 if ans == D else ans
