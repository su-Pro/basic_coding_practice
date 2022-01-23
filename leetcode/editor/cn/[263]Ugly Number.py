# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isUgly(self, n: int) -> bool:
        prime_list = [2, 3, 5]

        for prime in prime_list:

            # while n > 0 and n % prime is 0: n = int(n / prime)
            while n > 0 and n % prime is 0: n //= prime

        return n == 1
# leetcode submit region end(Prohibit modification and deletion)

# Solution().isUgly(6)