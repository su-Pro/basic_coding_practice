from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        group = s.split(":")
        ch_s, ch_e = group[0][0], group[1][0]

        repeat_s, repeat_e = int(group[0][1]), int(group[1][1])

        ans = []

        for c in range(ord(ch_s), ord(ch_e) + 1):
            current_c = chr(c)
            # fill ans
            for i in range(repeat_s, repeat_e + 1):
                ans.append(current_c + str(i))

        return ans


Solution().cellsInRange(
# "K1:L2"
"A1:F2"
)