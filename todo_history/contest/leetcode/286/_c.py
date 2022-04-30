from operator import le
from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ok_s_group = (intLength + 1) // 2
        ok_s_count = 10 ** (ok_s_group - 1) * 9
        ok_s_start = 10 ** (ok_s_count - 1)
        ans = []
        for q in queries:
            if q > ok_s_count:
                ans.append(-1)
            else:
                # 如何证明这里？
                l = str(ok_s_start + q - 1)
                r = l[::-1]
                if intLength % 2 == 0:
                    ans.append(int(l + r))
                else:
                    ans.append(int(l + r[1:]))
        return ans


Solution().kthPalindrome([2, 4, 6], 6)
