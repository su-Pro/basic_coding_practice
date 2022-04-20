# 典型DFS深搜路径...
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)

        def dfs(u, path):
            if u == n - 1:
                ans.append(path.copy())
                return
            # 遍历所有能到达的点，作为第一个落脚点
            for v in graph[u]:
                path.append(v)
                dfs(v, path)
                path.pop()

        dfs(0, [0])
        return ans
