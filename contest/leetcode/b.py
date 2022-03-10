from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        s = list(set(nums))
        s.sort()
        sum = 0
        count = 0
        idx = 1
        for v in s:
            for can_add in range(idx, v):
                sum += can_add
                count += 1
                if count == k:
                    print(sum)
                    return sum
            idx = v + 1
        while count != k:
            sum += idx
            count += 1
            idx += 1
        return sum
Solution().minimalKSum(
    #
    # [1, 4, 25, 10, 25],
    # 2
[5,6],
    6
)
