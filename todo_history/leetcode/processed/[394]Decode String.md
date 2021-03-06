<p>Given an encoded string, return its decoded string.</p>

<p>The encoding rule is: <code>k[encoded_string]</code>, where the <code>encoded_string</code> inside the square brackets is being repeated exactly <code>k</code> times. Note that <code>k</code> is guaranteed to be a positive integer.</p>

<p>You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.</p>

<p>Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, <code>k</code>. For example, there will not be input like <code>3a</code> or <code>2[4]</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;3[a]2[bc]&quot;
<strong>Output:</strong> &quot;aaabcbc&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;3[a2[c]]&quot;
<strong>Output:</strong> &quot;accaccacc&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;2[abc]3[cd]ef&quot;
<strong>Output:</strong> &quot;abcabccdcdcdef&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 30</code></li>
	<li><code>s</code> consists of lowercase English letters, digits, and square brackets <code>&#39;[]&#39;</code>.</li>
	<li><code>s</code> is guaranteed to be <strong>a valid</strong> input.</li>
	<li>All the integers in <code>s</code> are in the range <code>[1, 300]</code>.</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>递归</li><li>字符串</li></div></div><br><div><li>👍 1015</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
var decodeString = function (s) {
  // 思路：嵌套的运算符特点是计算完内部括号里的之后，会回过头再计算括号外的。
  // 这个结构其实就是很符合栈的不断往回头看的特性。

  /**
   * 和逆波兰表达式不一样的是 我们最终的计算结果并不是在stack中累积起来的。
   * 是要放回到tempStr中的。
   */
  const stack = [];
  let tempStr = "";
  let counter = 0;
  for (let i = 0; i < s.length; i++) {
    if (Number.isInteger(Number(s[i]))) {
      counter = counter * 10 + Number(s[i]);
    } else if (s[i] === "[") {
      stack.push(counter);
      stack.push(tempStr);
      counter = 0;
      tempStr = "";
    } else if (s[i] === "]") {
      tempStr = stack.pop() + tempStr.repeat(stack.pop());
    } else {
      tempStr += s[i];
    }
  }
  return tempStr;
};
```

```python3
class Solution:
    def decodeString(self, s: str) -> str:
        temp_str, stk, repeat_cunt = '', [], 0

        for ch in s:
            if ch.isdigit():
                repeat_cunt = repeat_cunt * 10 + int(ch)
            elif ch == '[':
                # 注意这里的顺序，先append repeat count num，想一下波兰表达式
                stk.append(repeat_cunt)
                stk.append(temp_str)

                temp_str = ''
                repeat_cunt = 0
            elif ch == ']':
                temp_str = stk.pop() + temp_str * stk.pop()
            else:
                temp_str += ch
        return temp_str

```
