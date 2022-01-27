<p>Design a max stack data structure that supports the stack operations and supports finding the stack&#39;s maximum element.</p>

<p>Implement the <code>MaxStack</code> class:</p>

<ul>
	<li><code>MaxStack()</code> Initializes the stack object.</li>
	<li><code>void push(int x)</code> Pushes element <code>x</code> onto the stack.</li>
	<li><code>int pop()</code> Removes the element on top of the stack and returns it.</li>
	<li><code>int top()</code> Gets the element on the top of the stack without removing it.</li>
	<li><code>int peekMax()</code> Retrieves the maximum element in the stack without removing it.</li>
	<li><code>int popMax()</code> Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the <strong>top-most</strong> one.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MaxStack&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;top&quot;, &quot;popMax&quot;, &quot;top&quot;, &quot;peekMax&quot;, &quot;pop&quot;, &quot;top&quot;]
[[], [5], [1], [5], [], [], [], [], [], []]
<strong>Output</strong>
[null, null, null, null, 5, 5, 1, 5, 1, 5]

<strong>Explanation</strong>
MaxStack stk = new MaxStack();
stk.push(5);   // [<strong><u>5</u></strong>] the top of the stack and the maximum number is 5.
stk.push(1);   // [<u>5</u>, <strong>1</strong>] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, <strong><u>5</u></strong>] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, <strong><u>5</u></strong>] the stack did not change.
stk.popMax();  // return 5, [<u>5</u>, <strong>1</strong>] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [<u>5</u>, <strong>1</strong>] the stack did not change.
stk.peekMax(); // return 5, [<u>5</u>, <strong>1</strong>] the stack did not change.
stk.pop();     // return 1, [<strong><u>5</u></strong>] the top of the stack and the max element is now 5.
stk.top();     // return 5, [<strong><u>5</u></strong>] the stack did not change.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>7</sup> &lt;= x &lt;= 10<sup>7</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, <code>peekMax</code>, and <code>popMax</code>.</li>
	<li>There will be <strong>at least one element</strong> in the stack when <code>pop</code>, <code>top</code>, <code>peekMax</code>, or <code>popMax</code> is called.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you come up with a solution that supports <code>O(1)</code> for each <code>top</code> call and <code>O(logn)</code> for each other call?&nbsp;<div><div>Related Topics</div><div><li>栈</li><li>设计</li><li>链表</li><li>双向链表</li><li>有序集合</li></div></div><br><div><li>👍 90</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```python3
class MaxStack:

    def __init__(self):
        self.stk = []
        self.stk_max = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        cnt = 0
        while len(self.stk_max) and x < self.stk_max[-1]:
            self.stk.append(self.stk_max.pop())
            cnt += 1

        self.stk_max.append(x)

        while cnt != 0:
            self.stk_max.append(self.stk.pop())
            cnt -= 1

    def pop(self) -> int:
        v = self.stk.pop()
        cnt = 0
        while len(self.stk_max) and v < self.stk_max[-1]:
            self.stk.append(self.stk_max.pop())
            cnt += 1

        self.stk_max.pop()

        while cnt != 0:
            self.stk_max.append(self.stk.pop())
            cnt -= 1
        return v

    def top(self) -> int:
        return self.stk[-1]

    def peekMax(self) -> int:
        return self.stk_max[-1]

    def popMax(self) -> int:
        # 同步减
        top_max = self.stk_max.pop()
        cnt = 0
        while self.stk[-1] != top_max:
            self.stk_max.append(self.stk.pop())
            cnt += 1
        # 同步减
        self.stk.pop()
        while cnt != 0:
            self.stk.append(self.stk_max.pop())
            cnt -= 1
        print(self.stk, self.stk_max)
        return top_max
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

```
  