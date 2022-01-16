# Given a string s, remove duplicate letters so that every letter appears once 
# and only once. You must make sure your result is the smallest in lexicographical 
# order among all possible results. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "bcabc"
# Output: "abc"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbacdcbc"
# Output: "acdb"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of lowercase English letters. 
#  
# 
#  
#  Note: This question is the same as 1081: https://leetcode.com/problems/
# smallest-subsequence-of-distinct-characters/ 
#  Related Topics 栈 贪心 字符串 单调栈 👍 643 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        visted = set()
        cntDict = collections.Counter(s)
        print(cntDict)
        for ch in s:
            # 如果已经检查存在栈中，则接续
            if ch in visted:
                cntDict[ch] -= 1
                continue

            while len(stk):
                t = stk[-1]
                if ord(ch) >= ord(t) or cntDict[t] <= 1: break
                cntDict[t] -= 1
                visted.remove(t)
                stk.pop()
            visted.add(ch)
            stk.append(ch)
        return ''.join(stk)

s = Solution()

s.removeDuplicateLetters('abcabc')
# leetcode submit region end(Prohibit modification and deletion)
