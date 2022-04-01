# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ln, st, ed, ans = len(s), 0, 0, 0

        while st < ln:
            seen = {}
            ed = st
            while ed >= 0 and s[ed] not in seen:
                seen.setdefault(s[ed], True)
                ed -= 1
            ans = max(ans, st - ed)
            st += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
