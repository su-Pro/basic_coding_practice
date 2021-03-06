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
<div><div>Related Topics</div><div><li>æ </li><li>å­ç¬¦ä¸²</li></div></div><br><div><li>ð 2934</li><li>ð 0</li></div> 
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
   * æè·¯ï¼ç»´æ¤ä¸ä¸ªæ  æ åéè¦pushå¥ç´§æ¥çéè¦è¿è¡éå¯¹çç¬¦å·
   * ä¾å¦ï¼'([' ä»å·¦å°å³éåæ°ç»æ¶ éè¦åæ'('å¡å¥æ åï¼ä¹ååå¡å¥'['ã
   *      å¦æä¸ä¸ä¸ªè¿­ä»£çè¯åå¥½è½åæ é¡¶çè¯è½matchä¸ é£ä¹æ é¡¶é¨åç´ å¯ä»¥popäºã
   *      å¨æ´ä¸ªè¿­ä»£ç»æä¹å å¦ææ æ¯ç©ºçç¶æä¸ååå¥çæ¯ ')','}',']' è¿å ä¸ªåç´  é£ä¹æä»¬å¯ä»¥æåç»æè¿­ä»£ã
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
    if (stack.length() === 0 && [')','}',']'].includes(arr[i])) {
      // è¿éæ ç©ºäº å¶å®æä»¬å¯ä»¥æåç»æ
	  return false;
	}
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
    1. æç¡®æ çç©çæ§è´¨ï¼ä¿çæææ²¡æè¢«å¹éè¿çç¬¦å·
    2. å¦ææç»éåå®æ°æ®ï¼åç°æ ä¸ä¸ºç©ºåè¯´ææéæ³å­ç¬¦ã

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
            if ch in chDict and stk and stk[-1] == chDict[ch]:  # å¤å®æ¯å¦è½æ¸é¤ä¸å¯¹ç¬¦å·
                stk.pop()
            else:
                stk.append(ch)
        return len(stk) is 0

```
