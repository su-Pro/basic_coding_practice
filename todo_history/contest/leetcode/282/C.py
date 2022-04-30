from typing import List


def getMinCnt(t, a):
    cnt = 0
    for v in a:
        if v <= t:
            cnt += v
        else:
            break
    return cnt


class Solution:

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        cnt = 0

        # 最坏情况，所需要的分钟数
        for t in range(1, time[0] * totalTrips + 1):
            s = 0

            for c in time:
                # 如果当前分钟不够开启，则什么也不做
                if c > t:
                    break
                else:
                    if s == totalTrips:
                        print(t)
                        return t
                    s += t // c


# Solution().minimumTime([1, 2, 3], 5)
# Solution().minimumTime([2], 1)
Solution().minimumTime([3, 3, 8], 9)
