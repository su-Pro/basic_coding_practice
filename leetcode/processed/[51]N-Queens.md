<p>The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an <code>n x n</code> chessboard such that no two queens attack each other.</p>

<p>Given an integer <code>n</code>, return <em>all distinct solutions to the <strong>n-queens puzzle</strong></em>. You may return the answer in <strong>any order</strong>.</p>

<p>Each solution contains a distinct board configuration of the n-queens&#39; placement, where <code>&#39;Q&#39;</code> and <code>&#39;.&#39;</code> both indicate a queen and an empty space, respectively.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> [[&quot;.Q..&quot;,&quot;...Q&quot;,&quot;Q...&quot;,&quot;..Q.&quot;],[&quot;..Q.&quot;,&quot;Q...&quot;,&quot;...Q&quot;,&quot;.Q..&quot;]]
<strong>Explanation:</strong> There exist two distinct solutions to the 4-queens puzzle as shown above
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [[&quot;Q&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>回溯</li></div></div><br><div><li>👍 1164</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
input your code
```

```python3
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        N = 20  # 注意数据范围
        res, chessboard, col, dig, udig = [], [['.'] * n for _ in range(n)], [False] * N, [False] * N, [False] * N

        def dfs(level: int):
            if level is n:
                res.append(list(map(lambda x: ''.join(x), chessboard)))
                return
            for i in range(0, n):
                if col[i] or dig[level + i] or udig[-level + i + n]: continue

                chessboard[level][i] = 'Q'
                col[i] = dig[level + i] = udig[i - level + n] = True
                dfs(level + 1)
                col[i] = dig[level + i] = udig[i - level + n] = False
                chessboard[level][i] = '.'

        dfs(0)
        return res



```
  