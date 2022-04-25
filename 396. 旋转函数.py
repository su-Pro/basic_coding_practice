class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * (n * 2 + 5)
        for i in range(1, n * 2 + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[(i - 1) % n]
        ans = 0  # 初始化窗口内的值
        for i in range(1, n + 1):
            ans += nums[i - 1] * (i - 1)
        # 开始滑动窗口
        l = n + 1
        cur = ans
        while l < 2 * n:
            cur += nums[(l - 1) % n] * (n - 1)
            cur -= pre_sum[l - 1] - pre_sum[l - n]
            ans = max(ans, cur)
            l += 1

        return ans
