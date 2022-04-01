# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ln, st, ed, ans = len(title), 0, 0, []

        while st < ln:
            ed = st
            while ed < ln and title[ed] != ' ': ed += 1

            # 后续处理，根据题意进行转化。
            if ed - st <= 2:
                ans.append(title[st:ed + 1].lower())
            else:
                ans.append(title[st:ed + 1].capitalize())
            # 确定指针如何移动
            st = ed + 1

        return "".join(ans)
# leetcode submit region end(Prohibit modification and deletion)
