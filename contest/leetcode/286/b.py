from typing import List


class Solution:
    def minDeletion(self, a: List[int]) -> int:
        ans, n = [], len(a)
        i = 0
        while i < n - 1:
            if a[i] == a[i + 1]:
                i += 1
            else:
                ans += [a[i], a[i + 1]]
                i += 2
        return n - len(ans)
