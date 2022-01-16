# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        dp = [''] * len(words)
        dp[0] = words[0]
        for i in range(1,len(words)):
            dp[i] = dp[i - 1] + words[i]

        for w in dp:
            if w == s: return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
