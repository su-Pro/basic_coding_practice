<p>Given two binary strings <code>a</code> and <code>b</code>, return <em>their sum as a binary string</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> a = "11", b = "1"
<strong>Output:</strong> "100"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> a = "1010", b = "1011"
<strong>Output:</strong> "10101"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> and <code>b</code> consist&nbsp;only of <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code> characters.</li>
	<li>Each string does not contain leading zeros except for the zero itself.</li>
</ul>
<div><div>Related Topics</div><div><li>位运算</li><li>数学</li><li>字符串</li><li>模拟</li></div></div><br><div><li>👍 732</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```python3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        ret = ''

        i = 0
        l_a = len(a)
        l_b = len(b)
        carry = 0
        while i < l_a or i < l_b:
            v_a = '0' if i >= l_a else a[i]
            v_b = '0' if i >= l_b else b[i]
            v_sum = int(v_a) + int(v_b) + int(carry)
            # 逢2进1
            carry = v_sum // 2
            v_sum %= 2
            ret += str(v_sum)
            i += 1

        # 如果还有进位的值
        if carry: ret += '1'
        return ret[::-1]

# 
```
  