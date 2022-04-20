from typing import List

N, D = 105, float('inf')


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist, vt, g = [D] * N, [False] * N, [[D] * N for x in range(N)]

        for u, v, z in times:
            g[u][v] = z

        def dijkstra():
            dist[k] = 0

            for _ in range(n):
                u = 0
                for _u in range(1, n + 1):
                    if not vt[_u] and (_u == 0 or dist[u] > dist[_u]):
                        u = _u
                vt[u] = True
                for v in range(1, n + 1):
                    dist[v] = min(dist[v], dist[u] + g[u][v])

        dijkstra()
        ans = 0
        for i in range(1, n + 1):
            if dist[i] == D:
                return -1
            ans = max(dist[i], ans)
        return ans


Solution().networkDelayTime(
    [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
    4,
    2
)
