from typing import List


class Solution:
    def findDifference(self, a: List[int], b: List[int]) -> List[List[int]]:
        a, b = set(a), set(b)
        return [
            [x for x in a if x not in b],
            [x for x in b if x not in a],
        ]
