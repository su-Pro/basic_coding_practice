from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        ans = 0
        st = set()

        for x, y in dig:
            st.add((x, y))

        for d in artifacts:
            canCover = True
            x1, y1, x2, y2 = d
            #     检查dig 中是否包含
            can = True
            for x in range(x1, x2 + 1):
                if not can: break
                for y in range(y1, y2 + 1):
                    if (x, y) not in st: can = False

            if can: ans += 1
        return ans
