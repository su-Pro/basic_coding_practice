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
var isPowerOfFour = function (n) {
  /**
   * ⚠️ 这里有一个有意思的地方 不要写反了判断顺序 判断顺序很重要
   * 得先判断是不是basecase 再判断是不是不符合条件之类的
   */
  // 如果n为1 则走到头了是2的幂
  if (n === 1) {
    return true;
  }
  // base case
  // 如果n为0 n除以4余数不为零 则不是4的幂
  if (n === 0 || n % 4 !== 0) {
    return false;
  }

  return isPowerOfFour(n / 4);
};
```

```python3
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 or n == 4:return True
        if n <= 0 or n % 4 != 0: return False

        return self.isPowerOfFour(n // 4)

```
