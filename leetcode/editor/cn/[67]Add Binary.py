# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        ret = ''

        i = 0
        l_a = len(a)
        l_b = len(b)
        carry = 0
        while i < l_a or i < l_b:
            v_a = '0' if i >= l_a else a[i]
            v_b = '0' if i >= l_b else b[i]
            v_sum = int(v_a) + int(v_b) + int(carry)
            # 逢2进1
            carry = v_sum // 2
            v_sum %= 2
            ret += str(v_sum)
            i += 1

        # 如果还有进位的值
        if carry: ret += '1'
        return ret[::-1]

# # leetcode submit region end(Prohibit modification and deletion)
#
# Solution().addBinary(
#     '11',
#     '1'
# )