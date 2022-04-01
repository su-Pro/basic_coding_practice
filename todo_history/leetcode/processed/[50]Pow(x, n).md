<p>Implement <a href="http://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(x, n)</a>, which calculates <code>x</code> raised to the power <code>n</code> (i.e., <code>x<sup>n</sup></code>).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = 10
<strong>Output:</strong> 1024.00000
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 2.10000, n = 3
<strong>Output:</strong> 9.26100
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = -2
<strong>Output:</strong> 0.25000
<strong>Explanation:</strong> 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-100.0 &lt; x &lt; 100.0</code></li>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup>-1</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sup>n</sup> &lt;= 10<sup>4</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>递归</li><li>数学</li></div></div><br><div><li>👍 854</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
var myPow = function (x, n) {
  function pow(x, n) {
    if (n === 0) {
      return 1;
    }
    // 最直接的方案是 myPow(x, n-1) * x
    /**
     * 将问题通过二分法来解决 往往能极大的降低时间复杂度
     * 不一定非要除以2，还可以除以3或者更大的数字 例如10。
     * 但带来的问题是需要处理的case就比较多了。一般二分法基本足够了。
     */
    const halfResult = myPow(x, Math.floor(n / 2));
    return n % 2 === 1 ? halfResult * halfResult * x : halfResult * halfResult;
  }
  // 不能一股脑的直接乘 因为n有可能为负数 这时候需要做个简单的数学变换就可以了。
  // x^(-2) = 1/x^2
  return n > 0 ? pow(x, n) : 1 / pow(x, -n);
};
/**
 * Time = O(log(n))
 * Space = O(log(n))
 */
```

```python3
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
                    n^10
                /       \
            n^5    x    n^5
        /       \
      n^2  xnx   n^2
    /  \
   n  x n
1 x n
        """

        def quickPow(x: float, n: int):
            if n is 0:
                return 1
            half_value = quickPow(x, n // 2)
            return half_value * half_value if n % 2 == 0 else half_value * half_value * x

        return 1 / quickPow(x, -n) if n < 0 else quickPow(x, n)

```
