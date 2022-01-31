<p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
</ol>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()[]{}&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(]&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>字符串</li></div></div><br><div><li>👍 2934</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
/**
  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

  An input string is valid if:
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
 */
function isValid(str) {
  /**
   * 思路：维护一个栈 栈内需要push入紧接着需要进行配对的符号
   * 例如： '([' 从左到右遍历数组时 需要先把'('塞入栈内，之后再塞入'['。
   *         如果下一个迭代的词刚好能和栈顶的词能match上 那么栈顶部元素可以pop了。
   */
  if (str.length === 0) {
    return true;
  }
  const charactersMap = {
    "(": ")",
    "{": "}",
    "[": "]",
  };
  const arr = str.split("");
  const stack = new Stack();
  stack.push(arr[0]);
  for (let i = 1; i < arr.length; i++) {
    if (charactersMap[stack.peek()] === arr[i]) {
      stack.pop();
    } else {
      stack.push(arr[i]);
    }
  }
  return stack.length() === 0;
}
```

```python3
class Solution:
    """
    1. 明确栈的物理性质：保留所有没有被匹配过的符号
    2. 如果最终遍历完数据，发现栈不为空则说明有非法字符。

    case
         "(" ->
         ")" ->
         "()" ->
         "()" ->
         "(]" ->
    """
    def isValid(self, s: str) -> bool:
        chDict, stk = {')': '(', '}': '{', ']': '['}, []
        for ch in s:
            if ch in chDict and stk and stk[-1] == chDict[ch]:  # 判定是否能清除一对符号
                stk.pop()
            else:
                stk.append(ch)
        return len(stk) is 0

```
