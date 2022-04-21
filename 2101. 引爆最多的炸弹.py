from typing import List

N = 105


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        n = len(bombs)
        graph = [[False] * N for x in range(N)]

        def dfs(u):
            vt[u] = True
            cnt = 1
            for v in range(n):
                if graph[u][v] and not vt[v]:
                    vt[v] = True
                    cnt += dfs(v)
            return cnt

        # 1. build graph , if u can bomb v
        for u in range(n):
            for v in range(n):
                ux, uy, ur = bombs[u]
                vx, vy, vr = bombs[v]
                if u != v and ((ux - vx) * (ux - vx) + (uy - vy) * (uy - vy) <= ur * ur):
                    graph[u][v] = True

        # 2. 以每个起点进行查找联通数量
        ans = 0
        for u in range(n):
            vt = [False] * N
            ans = max(ans, dfs(u))

        return ans


Solution().maximumDetonation([[2, 1, 3], [6, 1, 4]])
