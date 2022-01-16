# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ret = [0] * l
        stk = []
        for i, v in enumerate(temperatures):

            while len(stk) > 0 and stk[-1][0] < v:
                t = stk.pop()
                ret[t[1]] = i - t[1]
            stk.append((v, i))

        return ret
# leetcode submit region end(Prohibit modification and deletion)
