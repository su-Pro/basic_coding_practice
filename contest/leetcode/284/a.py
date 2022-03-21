from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idx = []
        for i, v in enumerate(nums):
            if v == key: idx.append(i)

        ans = set()
        for i, v in enumerate(nums):
            for _i in idx:
                if abs(i - _i) <= k: ans.add(i)
        print(ans)
        return list(ans)