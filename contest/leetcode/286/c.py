from math import fabs, floor
from typing import List


def isOk(v):
    t = str(v)
    for i in range(len(t) // 2):
        if t[i] != t[-i - 1]:
            return False
    return True


def getTotal(b):
    ans = None
    if b % 2 == 0:
        ans = [[0] * b for _ in range((pow(9, b // 2)))]
    else:
        ans = [[0] * b for _ in range((pow(9, b // 2) * 10))]

        for str_idx in range(floor(b / 2)):
            if str_idx % 2 != 0:
                for v in range(10):
                    for i in range(len(ans)):
                        ans[i][str_idx] = v
                        ans[i][- str_idx - 1] = v
            else:
                for v in range(1, 10):
                    for i in range(len(ans)):
                        ans[i][str_idx] = v
                        ans[i][-str_idx - 1] = v
    return ans


class Solution:
    def kthPalindrome(self, queries: List[int], b: int) -> List[int]:
        # l, r = pow(10, b - 1), pow(10, b)
        all = getTotal(b)
        ans = []
        for idx in queries:
            if idx - 1 < len(all):
                ans.append(all[idx - 1])
            else:
                ans.append(-1)
        return ans


Solution().kthPalindrome(
    [109883145, 67184890, 615116035, 730676834, 13, 700172947],
    3
)
