from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        solutions, n = set(), len(nums)
        for st in range(n):
            cnt = 0
            for ed in range(st, n):
                if nums[ed] % p == 0:
                    cnt += 1
                    if cnt > k:
                        break
                solutions.add(tuple(nums[st:ed + 1]))

        return len(solutions)


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        cols = set()

        def dfs(st, cur_k, path):
            if st >= len(nums) or cur_k + (nums[st] % p == 0) > k:
                return
            path.append(nums[st])
            if len(path) > 0:
                cols.add(tuple(path))
            dfs(st + 1, cur_k + (nums[st] % p == 0), path)

        for st in range(len(nums)):
            dfs(st, 0, [])

        return len(cols)


Solution().countDistinct(
    [10, 2, 17, 7, 20],
    1,
    10
)

print(set([('a', 'b'), ('a', 'b'), ('b', 'a')]))
print(set([('aa', 'bb'), ('a', 'b')]))
print(set([(1, 2), (1, 2), (2, 1), (1)]))
