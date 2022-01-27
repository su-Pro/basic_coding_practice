# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def is_upper(latter: str) -> bool:
            return 'A' <= latter <= 'Z'

        small_cnt = 0

        for ch in word:
            if is_upper(ch):
                small_cnt += 1

        return small_cnt == len(word) or small_cnt is 0 or (small_cnt == 1 and is_upper(word[0]))
# leetcode submit region end(Prohibit modification and deletion)
