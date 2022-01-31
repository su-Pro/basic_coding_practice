<p>Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (<code>push</code>, <code>peek</code>, <code>pop</code>, and <code>empty</code>).</p>

<p>Implement the <code>MyQueue</code> class:</p>

<ul>
	<li><code>void push(int x)</code> Pushes element x to the back of the queue.</li>
	<li><code>int pop()</code> Removes the element from the front of the queue and returns it.</li>
	<li><code>int peek()</code> Returns the element at the front of the queue.</li>
	<li><code>boolean empty()</code> Returns <code>true</code> if the queue is empty, <code>false</code> otherwise.</li>
</ul>

<p><strong>Notes:</strong></p>

<ul>
	<li>You must use <strong>only</strong> standard operations of a stack, which means only <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack&#39;s standard operations.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyQueue&quot;, &quot;push&quot;, &quot;push&quot;, &quot;peek&quot;, &quot;pop&quot;, &quot;empty&quot;]
[[], [1], [2], [], [], []]
<strong>Output</strong>
[null, null, null, 1, 1, false]

<strong>Explanation</strong>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>At most <code>100</code>&nbsp;calls will be made to <code>push</code>, <code>pop</code>, <code>peek</code>, and <code>empty</code>.</li>
	<li>All the calls to <code>pop</code> and <code>peek</code> are valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you implement the queue such that each operation is <strong><a href="https://en.wikipedia.org/wiki/Amortized_analysis" target="_blank">amortized</a></strong> <code>O(1)</code> time complexity? In other words, performing <code>n</code> operations will take overall <code>O(n)</code> time even if one of those operations may take longer.</p>
<div><div>Related Topics</div><div><li>栈</li><li>设计</li><li>队列</li></div></div><br><div><li>👍 546</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
class QueueImpelementedByStak {
  constructor() {
    // stack1 作为缓存栈 接受所有的输入
    this.stack1 = new Stack();
    // stack2 中元素经过“左右导右手” 就可以将最先进入栈的元素置顶到栈顶
    this.stack2 = new Stack();
  }

  push(num) {
    this.stack1.push(num);
  }

  pop() {
    if (this.empty()) {
      return;
    }
    if (this.stack2.isEmpty()) {
      this.wrap();
    }
    return this.stack2.pop();
  }

  peek() {
    if (this.empty()) {
      return;
    }
    if (this.stack2.isEmpty()) {
      this.wrap();
    }
    return this.stack2.peek();
  }

  wrap() {
    // 执行“左手导右手”操作
    while (!this.stack1.isEmpty()) {
      this.stack2.push(this.stack1.pop());
    }
  }

  empty() {
    return this.stack1.isEmpty() && this.stack2.isEmpty();
  }
}

/** ------------------------------------------------------ **/
/**
 * 其实两个stack就可以模拟dequeue
 * 因为两个stack可以成为一个queue 并且stack可以pop 也可以push 这不就是一个dequeue了吗
 * 但问题是在一个栈空了 再进行pop时 必须得把另外一个栈全部压进来 严重影响性能。
 * 怎么样才能避免把全部栈都压过去？
 */
class DeQueueWithThreeStack {
  constructor() {
    this.stackL = new Stack();
    this.stackR = new Stack();
    this.bufferStack = new Stack();
  }

  leftPush(elem) {
    this.stackL.push(elem);
  }
  rightPush(elem) {
    this.stackR.push(elem);
  }
  leftPop() {
    if (this.stackL.isEmpty()) {
      if (this.stackR.isEmpty()) {
        return null;
      }
      const halfLenth = Math.floor(this.stackR.length() / 2);
      // 在左右导右手的过程当中 bufferStack 作为缓冲buffer接受stackR前一半栈内元素
      // 剩下的底部一半 就导到stackL了
      // 最后导入完 再把bufferStack中的元素归位 就可以成功的把一个fullStack切为一半一半了
      while (this.stackR.length() >= halfLenth) {
        this.bufferStack.push(this.stackR.pop());
      }
      while (!this.stackR.isEmpty()) {
        this.stackL.push(this.stackR.pop());
      }
      while (!this.bufferStack.isEmpty()) {
        this.stackR.push(this.bufferStack.pop());
      }
    }
    return this.stackL.pop();
  }
  rightPop() {
    if (this.stackR.isEmpty()) {
      if (this.stackL.isEmpty()) {
        return null;
      }
      const halfLenth = Math.floor(this.stackL.length() / 2);
      while (this.stackL.length() >= halfLenth) {
        this.bufferStack.push(this.stackL.pop());
      }
      while (!this.stackL.isEmpty()) {
        this.stackR.push(this.stackL.pop());
      }
      while (!this.bufferStack.isEmpty()) {
        this.stackL.push(this.bufferStack.pop());
      }
    }
    return this.stackR.pop();
  }
}
```

```python3
class MyQueue:

    def __init__(self):
        # stk1 物理意义：Buff pushing elms
        # stk2 物理意义：Popping elms and run peek operate
        self.stk1, self.stk2 = [], []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        if not self.stk2: self.moved()
        return -1 if not self.stk2 else self.stk2.pop()

    def peek(self) -> int:
        if not self.stk2: self.moved()
        return -1 if not self.stk2 else self.stk2[-1]

    def empty(self) -> bool:
        return (not self.stk1) and (not self.stk2)

    def moved(self) -> None:
        # moved all elm stk1 to stk2
        if not self.stk2:
            while self.stk1: self.stk2.append(self.stk1.pop())

            # Your MyQueue object will be instantiated and called as such:
            # obj = MyQueue()
            # obj.push(x)
            # param_2 = obj.pop()
            # param_3 = obj.peek()
            # param_4 = obj.empty()

```
