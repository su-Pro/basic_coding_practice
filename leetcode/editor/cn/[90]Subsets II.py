# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = []

        def dfs(choose, level, path):
            if level == len(nums):
                s.append(path.copy())
                return

            dfs(False, level + 1, path)
            # 减枝操作时候，尽可能的在状态变化前做，这样能够避免奇奇怪怪的状态不一致问题
            if not choose and level > 0 and nums[level - 1] == nums[level]:
                return
            path.append(nums[level])
            dfs(True, level + 1, path)
            path.pop()

        dfs(False, 0, [])

        return s
# leetcode submit region end(Prohibit modification and deletion)
