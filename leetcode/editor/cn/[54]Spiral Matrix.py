# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        # (x,y) 上 右 下 左
        direction, visited, ret = [(-1, 0), (0, 1), (1, 0), (0, -1)], [[False for x in range(n)] for y in range(m)], []

        cur_x, cur_y, cur_d = 0, 0, 1  # 要先从左到右来

        for i in range(m * n):
            ret.append(matrix[cur_x][cur_y])
            visited[cur_x][cur_y] = True

            n_x, n_y = cur_x + direction[cur_d][0], cur_y + direction[cur_d][1]
            # 检查是否非法访问
            if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or visited[n_x][n_y]:
                # 往下一个方向转动～
                cur_d = (cur_d + 1) % 4
                n_x, n_y = cur_x + direction[cur_d][0], cur_y + direction[cur_d][1]

            cur_x = n_x
            cur_y = n_y

        return ret


# leetcode submit region end(Prohibit modification and deletion)

# Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
