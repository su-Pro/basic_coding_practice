# There are n cities connected by some number of flights. You are given an 
# array flights where flights[i] = [fromi, toi, pricei] indicates that there is a 
# flight from city fromi to city toi with cost pricei. 
# 
#  You are also given three integers src, dst, and k, return the cheapest price 
# from src to dst with at most k stops. If there is no such route, return -1. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k =
#  1
# Output: 200
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as 
# marked red in the picture.
#  
# 
#  Example 2:
# 
#  
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k =
#  0
# Output: 500
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as 
# marked blue in the picture.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 100 
#  0 <= flights.length <= (n * (n - 1) / 2) 
#  flights[i].length == 3 
#  0 <= fromi, toi < n 
#  fromi != toi 
#  1 <= pricei <= 10⁴ 
#  There will not be any multiple flights between two cities. 
#  0 <= src, dst, k < n 
#  src != dst 
#  
#  Related Topics 深度优先搜索 广度优先搜索 图 动态规划 最短路 堆（优先队列） 👍 438 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import OrderedDict, deque, defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights.sort(key=lambda f: f[0])
        # 1. 建图
        # TODO: 如何给dict增加类型呢？
        g = defaultdict()
        for f in flights:
            s, e, p = f
            if s not in g:
                g[s] = []
            g[s].append((e, p))

        # 2. BFS
        q = deque([(src, 0)])

        level = 0
        min_v = float('inf')
        visited = [float('inf')] * n
        while len(q) != 0 and level <= k + 1:

            q_len = len(q)
            for _ in range(q_len):
                curId, cost = q.popleft()
                if cost != 0:
                    visited[curId] = cost
                if curId == dst:
                    min_v = min(min_v, cost)
                else:
                    neighbors = g.get(curId, [])
                    for nextId, nextCost in neighbors:
                        if nextCost + cost < visited[nextId]: q.append((nextId, nextCost + cost))
            level += 1

        return min_v if min_v != float('inf') else -1

# leetcode submit region end(Prohibit modification and deletion)
