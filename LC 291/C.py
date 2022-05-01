from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        idxs = []
        cols = set()
        for i, ch in enumerate(nums):
            if ch % p == 0: idxs.append(i)

        def dfs(st, cur_k, path):
            if st >= len(nums): return
            if cur_k + (nums[st] % p == 0) > k: return
            path.append(nums[st])
            if len(path) != 0: cols.add(tuple(path))
            dfs(st + 1, cur_k + (nums[st] % p == 0), path)

        for st in range(len(nums)):
            dfs(st, 0, [])

        return len(cols)


Solution().countDistinct(
    [10, 2, 17, 7, 20],
    1,
    10
)
