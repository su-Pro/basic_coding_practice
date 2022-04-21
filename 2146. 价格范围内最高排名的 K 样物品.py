from typing import List
import collections
# 最短路变形
# 1. flood-fill 求出最短路
# 2. 按照要求输出相应的格子

dx, dy = (-1, 0, 0, 1), (0, -1, 1, 0)


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        n, m, ans = len(grid), len(grid[0]), []
        upper, lower = pricing

        que, vt = collections.deque([(0, tuple(start))]), [
            [False] * m for x in range(n)]

        def isok(x, y):
            return 0 <= x < n and 0 <= y < m and grid[x][y] != 0 and not vt[nx][ny]

        while que and len(ans) < k:
            d, [x, y] = que.popleft()
            if upper <= grid[x][y] <= lower:
                ans.append((x, y))
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not isok(nx, ny):
                    continue
                que.append((d + 1, (nx, ny)))
                vt[nx][ny] = True
        ans.sort(lambda x: grid[x[0]][x[1]])
        return ans


Solution().highestRankedKItems([[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]], [2, 5],
                               [0, 0], 3)
