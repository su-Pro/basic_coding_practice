<p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of four. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of four, if there exists an integer <code>x</code> such that <code>n == 4<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 16
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> false
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?<div><div>Related Topics</div><div><li>位运算</li><li>递归</li><li>数学</li></div></div><br><div><li>👍 286</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
input your code
```

```python3
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 or n == 4:return True
        if n <= 0 or n % 4 != 0: return False

        return self.isPowerOfFour(n // 4)

```
  