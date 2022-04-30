import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        c_s = collections.Counter(s)
        t_s = collections.Counter(t)

        for k, v in c_s.items():
            if not t_s.get(k):
                ans += v
                continue
            ans += abs(v - t_s[k])
            # del c_s[k]
            del t_s[k]
        for k, v in t_s.items():
            if not c_s.get(k): ans += v
        return ans


Solution().minSteps("leetcode", "coats")
Solution().minSteps("night", "thing")
Solution().minSteps("cotxazilut", "nahrrmcchxwrieqqdwdpneitkxgnt")
