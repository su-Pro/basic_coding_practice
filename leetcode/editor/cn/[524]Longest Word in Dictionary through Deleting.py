# leetcode submit region begin(prohibit modification and deletion)


class Solution:

    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        def isSubSequence(a, b):
            l_a, l_b, i, j = len(a), len(b), 0, 0

            while i < l_a and j < l_b:
                if a[i] == b[j]: j += 1
                i += 1

            return j == l_b

        ret = ''

        for target in dictionary:
            if not isSubSequence(s, target): continue
            if (not ret) or len(ret) < len(target) or (len(ret) == len(target) and target < ret):
                ret = target
        return ret
# leetcode submit region end(prohibit modification and deletion)
