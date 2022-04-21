import collections
from typing import List

N, D = int(1e3 + 5), float('inf')


# 裸bfs状态题


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        def isok(case):
            return 0 <= case <= 1000 and dist[case] == D

        # que里存储的元素类型：
        que, dist = collections.deque([(0, start)]), [D] * N
        dist[start] = 0
        while que:
            d, u = que.popleft()
            # 这里不需要考虑nums中数字用的次数，所以就无脑循环即可
            for num in nums:
                for v in [u + num, u - num, u ^ num]:
                    if v == goal: return d + 1
                    if not isok(v): continue
                    dist[v] = d + 1
                    que.append((dist[v], v))

        return -1
