from typing import List
import collections

N = int(1e3 + 5)
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        que, dist = collections.deque(), [[float('inf')] * m for x in range(n)]

        def isok(x, y):
            return 0 <= x < n and 0 <= y < m and dist[x][y] == float('inf') and isWater[x][y] == 0

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    dist[i][j] = 0
                    que.append((i, j))

        while que:
            x, y = que.popleft()
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if not isok(nx, ny): continue
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))

        return dist
