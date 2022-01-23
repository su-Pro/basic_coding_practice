# recommend: 🌟🌟🌟🌟
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(x, y, u):
            if u >= len(word): return True
            direction_x, direction_y = (-1, 0, 1, 0), (0, 1, 0, -1)
            visted[x][y] = True
            for d in range(4):
                new_x, new_y = x + direction_x[d], y + direction_y[d]
                # 判断是否满足范围
                if 0 <= new_x < m and \
                        0 <= new_y < n and \
                        not visted[new_x][new_y] and \
                        board[new_x][new_y] == word[u]:
                    if dfs(new_x, new_y, u + 1): return True
            # 只确保当前这轮搜索，不会重复走。
            # 如果没有找到最终路径，下一轮搜索还要重复尝试的！
            # 例如case: [["C","A","A"],["A","A","A"],["B","C","D"]] "AAB"
            visted[x][y] = False

            return False

        m, n = len(board), len(board[0])
        visted = [[False for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1): return True

        return False

# leetcode submit region end(Prohibit modification and deletion)
# Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],'ABCCED')