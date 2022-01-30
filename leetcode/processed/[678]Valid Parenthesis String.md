<p>Given a string <code>s</code> containing only three types of characters: <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code> and <code>&#39;*&#39;</code>, return <code>true</code> <em>if</em> <code>s</code> <em>is <strong>valid</strong></em>.</p>

<p>The following rules define a <strong>valid</strong> string:</p>

<ul>
	<li>Any left parenthesis <code>&#39;(&#39;</code> must have a corresponding right parenthesis <code>&#39;)&#39;</code>.</li>
	<li>Any right parenthesis <code>&#39;)&#39;</code> must have a corresponding left parenthesis <code>&#39;(&#39;</code>.</li>
	<li>Left parenthesis <code>&#39;(&#39;</code> must go before the corresponding right parenthesis <code>&#39;)&#39;</code>.</li>
	<li><code>&#39;*&#39;</code> could be treated as a single right parenthesis <code>&#39;)&#39;</code> or a single left parenthesis <code>&#39;(&#39;</code> or an empty string <code>&quot;&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "(*)"
<strong>Output:</strong> true
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "(*))"
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code> or <code>&#39;*&#39;</code>.</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>贪心</li><li>字符串</li><li>动态规划</li></div></div><br><div><li>👍 443</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
input your code
```

```python3
class Solution:
    def checkValidString(self, s: str) -> bool:
        stk1, stk2 = [], []

        # 保证没有 ）在 （ 前的case
        for i, v in enumerate(s):
            if v == '(':
                stk1.append(i)
            elif v == '*':
                stk2.append(i)
            elif v == ')' and len(stk1):
                stk1.pop()  # 消除case1：该"）"左侧有"（"
            elif v == ')' and len(stk2):
                stk2.pop()  # 消除case1：该"）"左侧有"*"
            else:
                return False

        # 特殊case： 用 * 消除 (
        i, j = len(stk1) - 1, len(stk2) - 1

        while i >= 0 and j >= 0:
            if stk1[i] > stk2[j]: return False
            i -= 1
            j -= 1

        # 只有所有（ 被消除才能符合有效性质，因为 * 可以作为空串存在
        return i < 0

```
  