from typing import List


# 图的最基本flood-fill

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = int(1e3 + 5)
        n = len(rooms)
        vt = [False] * N

        def dfs(u):
            if vt[u]: return
            vt[u] = True
            for v in rooms[u]:
                dfs(v)

        dfs(0)

        for i in range(n):
            if not vt[i]: return False
        return True
