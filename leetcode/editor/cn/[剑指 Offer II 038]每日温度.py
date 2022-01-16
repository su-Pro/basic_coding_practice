# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ret = [0] * l
        stk = []

        for i in range(l):
            while len(stk) and temperatures[stk[-1]] < temperatures[i]:
                t = temperatures.pop()
                stk[t] = i - t
            stk.append(i)

        return ret
# leetcode submit region end(Prohibit modification and deletion)
