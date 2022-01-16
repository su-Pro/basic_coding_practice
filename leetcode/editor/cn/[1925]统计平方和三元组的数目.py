# 一个 平方和三元组 (a,b,c) 指的是满足 a² + b² = c² 的 整数 三元组 a，b 和 c 。 
# 
#  给你一个整数 n ，请你返回满足 1 <= a, b, c <= n 的 平方和三元组 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 5
# 输出：2
# 解释：平方和三元组为 (3,4,5) 和 (4,3,5) 。
#  
# 
#  示例 2： 
# 
#  输入：n = 10
# 输出：4
# 解释：平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 250 
#  
#  Related Topics 数学 枚举 👍 7 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def countTriples(self, n: int) -> int:
    #     cnt = 0
    #     for i in range(1, n + 1):
    #         for j in range(i + 1, n):
    #             for k in range(j + 1, n + 1):
    #                 if i * i + j * j == k * k: cnt += 2
    #     return cnt

    def countTriples(self, n: int) -> int:
        cnt = 0
        sums = [i * i for i in range(1, n + 1)]
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if i * i + j * j in sums: cnt += 2
        return cnt


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
s.countTriples(5)
