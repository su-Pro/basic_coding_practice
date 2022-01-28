<p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the</em> <code>matrix</code> <em>in spiral order</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>矩阵</li><li>模拟</li></div></div><br><div><li>👍 967</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        # (x,y) 上 右 下 左
        direction, visited, ret = [(-1, 0), (0, 1), (1, 0), (0, -1)], [[False for x in range(n)] for y in range(m)], []

        cur_x, cur_y, cur_d = 0, 0, 1  # 要先从左到右来

        for i in range(m * n):
            ret.append(matrix[cur_x][cur_y])
            visited[cur_x][cur_y] = True

            n_x, n_y = cur_x + direction[cur_d][0], cur_y + direction[cur_d][1]
            # 检查是否非法访问
            if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n or visited[n_x][n_y]:
                # 往下一个方向转动～
                cur_d = (cur_d + 1) % 4
                n_x, n_y = cur_x + direction[cur_d][0], cur_y + direction[cur_d][1]

            cur_x = n_x
            cur_y = n_y

        return ret



```
  