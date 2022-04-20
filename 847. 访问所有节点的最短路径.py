import collections
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N, D, n = 12 + 5, float('inf'), len(graph)
        mask = 1 << n
        dist = [[D] * N for x in range(mask)]

        que = collections.deque()
        # 所有可能的状态:
        for i in range(n):
            dist[1 << i][i] = 0
            que.append((1 << i, i))

        while que:
            state, u = que.popleft()
            # 这里状态相等的情况下，为什么是mask - 1？
            step = dist[state][u]
            if state == mask - 1: return step
            # 搜索相邻一层的状态
            for v in graph[u]:
                # 如果当前点还没有被访问到
                if dist[state | 1 << v][v] == D:
                    dist[state | 1 << v][v] = step + 1
                    que.append((state | 1 << v, v))
        return -1
