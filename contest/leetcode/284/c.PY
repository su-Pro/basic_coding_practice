import collections
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        cur_max = 0
        cur_collection = {}
        for i, v in enumerate(nums):
            if v not in cur_collection: cur_collection[v] = 0
            if k == 0: break
            top = nums[0]
            if k == 1 and cur_max > k[1] and counter[cur_max] == 0:
                nums.append(cur_max)
                break

            else:
                # D 逻辑
                cur_collection[top] += 1
                counter[top] -= 1
                cur_max = max(cur_max, top)
                nums.pop(0)

            k -= 1
        print(nums)


Solution().maximumTop(
    [5, 2, 2, 4, 0, 6],
    4
)
