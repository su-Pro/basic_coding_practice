import collections
from typing import List

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N = 105


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n, m = len(maze), len(maze[0])

        # 可以继续走下去吗？
        def next_can_go(x, y, di):
            nx, ny = x + dx[di], y + dy[di]
            return 0 <= nx < n and 0 <= ny < m and (maze[nx][ny] == 0)

        # 队列里存储的是，停下准备往不同方向走的时候的位置
        que, vt = collections.deque([tuple(start)]), [[False] * N for x in range(N)]
        vt[start[0]][start[1]] = True
        while que:
            x, y = que.popleft()
            if x == destination[0] and y == destination[1]: return True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < n and 0 <= ny < m and not vt[nx][ny] and maze[nx][ny] == 0): continue
                while next_can_go(nx, ny, i):
                    nx, ny = nx + dx[i], ny + dy[i]
                if not vt[nx][ny]:
                    que.append((nx, ny))
                    vt[nx][ny] = True

        return False
