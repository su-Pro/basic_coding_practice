# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


def getOneCnt(n: int):
    cnt,N = 0,n
    while n:
        n -= n & -n
        cnt += 1
    return cnt,N


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=getOneCnt)
        return arr
# leetcode submit region end(Prohibit modification and deletion)
