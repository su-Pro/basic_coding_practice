<p>Evaluate the value of an arithmetic expression in <a href="http://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">Reverse Polish Notation</a>.</p>

<p>Valid operators are <code>+</code>, <code>-</code>, <code>*</code>, and <code>/</code>. Each operand may be an integer or another expression.</p>

<p><strong>Note</strong> that division between two integers should truncate toward zero.</p>

<p>It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> tokens = [&quot;2&quot;,&quot;1&quot;,&quot;+&quot;,&quot;3&quot;,&quot;*&quot;]
<strong>Output:</strong> 9
<strong>Explanation:</strong> ((2 + 1) * 3) = 9
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> tokens = [&quot;4&quot;,&quot;13&quot;,&quot;5&quot;,&quot;/&quot;,&quot;+&quot;]
<strong>Output:</strong> 6
<strong>Explanation:</strong> (4 + (13 / 5)) = 6
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> tokens = [&quot;10&quot;,&quot;6&quot;,&quot;9&quot;,&quot;3&quot;,&quot;+&quot;,&quot;-11&quot;,&quot;*&quot;,&quot;/&quot;,&quot;*&quot;,&quot;17&quot;,&quot;+&quot;,&quot;5&quot;,&quot;+&quot;]
<strong>Output:</strong> 22
<strong>Explanation:</strong> ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tokens.length &lt;= 10<sup>4</sup></code></li>
	<li><code>tokens[i]</code> is either an operator: <code>&quot;+&quot;</code>, <code>&quot;-&quot;</code>, <code>&quot;*&quot;</code>, or <code>&quot;/&quot;</code>, or an integer in the range <code>[-200, 200]</code>.</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>数组</li><li>数学</li></div></div><br><div><li>👍 455</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
var evalRPN = function (tokens) {
  // 这道题其实更多的是考验程序编写能力
  // all operators "+", "-", "*", "/".
  const stack = new Stack();
  for (let i = 0; i < tokens.length; i++) {
    const num = Number(tokens[i]);
    if (!Number.isNaN(num)) {
      stack.push(num);
      continue;
    }
    const num1 = stack.pop();
    const num2 = stack.pop();
    switch (tokens[i]) {
      case "+":
        stack.push(num2 + num1);
        break;
      case "-":
        stack.push(num2 - num1);
        break;
      case "*":
        stack.push(num2 * num1);
        break;
      case "/":
        // 这里的取整逻辑比较坑
        stack.push(
          num2 / num1 > 0 ? Math.floor(num2 / num1) : Math.ceil(num2 / num1)
        );
        break;
    }
  }
  return stack.pop();
};
```

```python3
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk, arithmetic_dict = [], {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}

        for ch in tokens:
            if ch not in arithmetic_dict:
                stk.append(int(ch))
            else:
                # NOTE: 四则运算，- 和 / 有顺序要求，注意这里v1 和 v2的顺序
                v2, v1 = stk.pop(), stk.pop()
                stk.append(arithmetic_dict[ch](v1, v2))

        return stk[-1]

```
