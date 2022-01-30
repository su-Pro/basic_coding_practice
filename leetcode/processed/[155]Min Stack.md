<p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>

<p>Implement the <code>MinStack</code> class:</p>

<ul>
	<li><code>MinStack()</code> initializes the stack object.</li>
	<li><code>void push(int val)</code> pushes the element <code>val</code> onto the stack.</li>
	<li><code>void pop()</code> removes the element on the top of the stack.</li>
	<li><code>int top()</code> gets the top element of the stack.</li>
	<li><code>int getMin()</code> retrieves the minimum element in the stack.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MinStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;getMin&quot;,&quot;pop&quot;,&quot;top&quot;,&quot;getMin&quot;]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>Output</strong>
[null,null,null,null,-3,null,0,-2]

<strong>Explanation</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Methods <code>pop</code>, <code>top</code> and <code>getMin</code> operations will always be called on <strong>non-empty</strong> stacks.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>getMin</code>.</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>设计</li></div></div><br><div><li>👍 1154</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
input your code
```

```python3

class MinStack:

    def __init__(self):
        self.min_stk, self.normal_stk = [], []

    def push(self, val: int) -> None:
        if not self.min_stk or self.min_stk[-1] > val:
            self.min_stk.append(val)
        else:
            self.min_stk.append(self.min_stk[-1])
        self.normal_stk.append(val)

    def pop(self) -> None:
        if self.normal_stk:
            self.normal_stk.pop()
            self.min_stk.pop()

    def top(self) -> int:
        if self.normal_stk: return self.normal_stk[-1]
        return -1

    def getMin(self) -> int:
        if self.min_stk: return self.min_stk[-1]
        return -1

#
#
#

class FollUpMinStack:

    def __init__(self):
        self.min_stk, self.normal_stk = [], []

    def push(self, val: int) -> None:
        self.normal_stk.append(val)

        if not self.min_stk or self.min_stk[-1][0] > val:
            self.min_stk.append((val, len(self.normal_stk)))
        else:
            return

    def pop(self) -> None:
        if not self.normal_stk:
            return
        self.normal_stk.pop()
        if self.min_stk[-1][1] > len(self.normal_stk): self.min_stk.pop()

    def top(self) -> int:
        if self.normal_stk: return self.normal_stk[-1]
        return -1

    def getMin(self) -> int:
        if self.min_stk: return self.min_stk[-1][0]
        return -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

```
  