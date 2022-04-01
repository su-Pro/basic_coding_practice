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
/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function (s) {
  /**
   * 思路：字符串中可能会出现'('，'*'，')'。
   * 不能单纯的使用一个栈来存储。
   * 再审一遍题目，从题目中可知：
   *     '*'可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串
   *     '*'可以有一个也可能是接连着出现很多个。"(**))"
   * 那么我们可以不可以用多个栈来解决这个问题？
   *
   * '('存一个栈，'*'存另外一个栈。之后再循环迭代
   */
  let stack1 = new Stack();
  let stack2 = new Stack();
  for (let i = 0; i < s.length; i++) {
    switch (s[i]) {
      case "(":
        // 注意⚠️ 这里应该把下标传递进去 后续会需要
        stack1.push(i);
        break;
      case "*":
        // 注意⚠️ 这里应该把下标传递进去 后续会需要
        stack2.push(i);
        break;
      case ")":
        if (stack1.length() === 0 && stack2.length() === 0) {
          // 栈空了 提前结束
          return false;
        }
        if (stack1.length()) {
          stack1.pop();
        } else {
          stack2.pop();
        }
        break;
    }
  }
  // stack1中的'('可以和'*'匹配 因此把它们匹配一遍
  /**
   * 注意⚠️ 这里*号必须出现在'('之后
   */
  while (!stack1.isEmpty() && !stack2.isEmpty()) {
    const index1 = stack1.pop();
    const index2 = stack2.pop();
    if (index1 >= index2) {
      return false;
    }
  }
  return stack1.length() === 0;
};
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
