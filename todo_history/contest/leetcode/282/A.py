from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for ch in words:
            if ch.startswith(pref):
                ans += 1

        return ans
