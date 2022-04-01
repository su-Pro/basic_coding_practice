from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []

        def solve(level, path, count):
            if level == len(word):
                if count > 0: path += str(count)
                ans.append(path)
                return
            solve(level + 1, path, count + 1)
            solve(level + 1, path + (str(count) if count > 0 else "") + word[level], 0)

        solve(0, "", 0)

        return ans
