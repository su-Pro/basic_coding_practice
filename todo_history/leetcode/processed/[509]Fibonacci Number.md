<p>The <b>Fibonacci numbers</b>, commonly denoted <code>F(n)</code> form a sequence, called the <b>Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is,</p>

<pre>
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>
<div><div>Related Topics</div><div><li>递归</li><li>记忆化搜索</li><li>数学</li><li>动态规划</li></div></div><br><div><li>👍 392</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
const hashmap = new Map();
var fib = function (n) {
  // base case
  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  // 因为这个recursion出现了两个分叉，因此会自然的会有多个重复计算的问题。
  // 例如 f(4) = f(3) + f(2)  f(5) = f(4) + f(3)
  // 因此利用一个hashmap进行存储 避免重复计算。
  if (hashmap.has(n)) {
    return hashmap.get(n);
  }
  hashmap.set(n, fib(n - 1) + fib(n - 2));
  return hashmap.get(n);
};
```

```python3
class Solution:
    """
           F(5)
        /        \
        F(4)     F(3)
    /     \
    F(3)   F(2)
   /   \
F(2)    F(1)

F(3) 是重复计算,我们要记录以及计算过的值。

记录一个值是否已经存在，并且在O（1）时间获取出值，可以使用hashTable
    """

    memo = {}

    def fib(self, n: int) -> int:
        if n is 0: return 0
        if n is 1 or n is 2: return 1
        if n in self.memo: return self.memo[n]

        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.memo[n]

```
