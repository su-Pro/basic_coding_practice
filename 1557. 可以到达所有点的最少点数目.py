from typing import List


class Solution:
    # 朴素的求出度0的点
    # def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    #     N = int(1e5) + 5
    #     in_degree = [-1] * N
    #     for u, v in edges:
    #         if in_degree[u] == -1:
    #             in_degree[u] = 0
    #         if in_degree[v] == -1:
    #             in_degree[v] = 0
    #         in_degree[v] += 1
    #
    #     ans = []
    #     for u_idx, in_d in enumerate(in_degree):
    #         if in_d == 0: ans.append(u_idx)
    #
    #     return ans

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        has_in_degree_set = set(v for u, v in edges)
        # 图中的节点，只要不在 has_in_degree_set 中，则说明 -> 没有入度 -> 入度为0
        return [u for u in range(n) if u not in has_in_degree_set]
