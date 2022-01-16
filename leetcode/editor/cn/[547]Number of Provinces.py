# There are n cities. Some of them are connected, while some are not. If city a 
# is connected directly with city b, and city b is connected directly with city c,
#  then city a is connected indirectly with city c. 
# 
#  A province is a group of directly or indirectly connected cities and no 
# other cities outside of the group. 
# 
#  You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the 
# iᵗʰ city and the jᵗʰ city are directly connected, and isConnected[i][j] = 0 
# otherwise. 
# 
#  Return the total number of provinces. 
# 
#  
#  Example 1: 
# 
#  
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 200 
#  n == isConnected.length 
#  n == isConnected[i].length 
#  isConnected[i][j] is 1 or 0. 
#  isConnected[i][i] == 1 
#  isConnected[i][j] == isConnected[j][i] 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 689 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt = 0
        visited = set()
        citys = len(isConnected)

        for c in range(citys):
            if c in visited: continue
            cnt += 1
            Q = collections.deque([c])
            # 遍历所有相连的城市，将其加入Q中
            while len(Q):
                j = Q.popleft()
                visited.add(j)
                for k in range(citys):
                    if isConnected[j][k] != 1 or k in visited: continue
                    Q.append(k)
        return cnt
# leetcode submit region end(Prohibit modification and deletion)
