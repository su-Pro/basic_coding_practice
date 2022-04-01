<p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of two. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of two, if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>0</sup> = 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup> = 16
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?<div><div>Related Topics</div><div><li>位运算</li><li>递归</li><li>数学</li></div></div><br><div><li>👍 457</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
function isPowerOfTwo(n) {
  // base case
  // 如果n为0 n除以2余数不为零 则不是2的幂
  if (n === 0 || n % 2 !== 0) {
    return false;
  }
  // 如果n为1 则走到头了是2的幂
  if (n === 1) {
    return true;
  }
  return isPowerOfTwo(n / 2);
}
```

```python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # base case:
        if n == 1 or n == 2: return True
        if n <= 0 or n % 2 != 0: return False

        # 数据范围如何缩减！
        return self.isPowerOfTwo(n // 2)


```
