# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        cnt = 0
        for c in s:
            if c == '[':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                res += 1
                cnt += 2

        return res
# leetcode submit region end(Prohibit modification and deletion)
