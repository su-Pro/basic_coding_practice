# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToBase7(self, num: int) -> str:
        ret = []
        flag = False
        if num < 0:
            flag = True
            num *= -1
        elif num == 0:
            return '0'

        while num is not 0:
            ret.append(str(num % 7))
            num //= 7

        ret.reverse()
        res = ''.join(ret)
        return res if not flag else '-' + res
    # leetcode submit region end(Prohibit modification and deletion)


# print(Solution().convertToBase7(-7))
