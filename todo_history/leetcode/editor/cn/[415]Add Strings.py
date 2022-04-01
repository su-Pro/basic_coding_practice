# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans, ln1, ln2, s1, s2 = [], len(num1), len(num2), num1[::-1], num2[::-1]

        i, payload = 0, 0
        while i < ln1 or i < ln2 or payload > 0:
            if i < ln1: payload += int(s1[i])
            if i < ln2: payload += int(s2[i])
            ans.append(payload % 10)
            payload //= 10
            i += 1

        ans = ans[::-1]
        return "".join(map(str, ans))
        # leetcode submit region end(Prohibit modification and deletion)
