# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = []
        cnt = collections.Counter(s)
        sorted_cnt = list(sorted(cnt.items(), key=lambda item: - ord(item[0])))

        for idx, pair in enumerate(sorted_cnt):
            while True:
                for _ in range(min(sorted_cnt[idx][1], repeatLimit)):
                    ans.append(pair[0])
                    sorted_cnt[idx] = (pair[0], sorted_cnt[idx][1] - 1)

                    # 用完
                if sorted_cnt[idx][1] == 0: break

                # 没用完，下一个元素补1
                if idx + 1 == len(sorted_cnt): break
                else:
                    ans.append(sorted_cnt[idx + 1][0])
                    sorted_cnt[idx + 1] = (sorted_cnt[idx + 1][0], sorted_cnt[idx + 1][1] - 1)

        return ''.join(ans)


# leetcode submit region end(Prohibit modification and deletion)
Solution().repeatLimitedString(
    "aababab",
    2
)
