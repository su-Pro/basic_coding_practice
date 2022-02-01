<p>In a linked list of size <code>n</code>, where <code>n</code> is <strong>even</strong>, the <code>i<sup>th</sup></code> node (<strong>0-indexed</strong>) of the linked list is known as the <strong>twin</strong> of the <code>(n-1-i)<sup>th</sup></code> node, if <code>0 &lt;= i &lt;= (n / 2) - 1</code>.</p>

<ul>
	<li>For example, if <code>n = 4</code>, then node <code>0</code> is the twin of node <code>3</code>, and node <code>1</code> is the twin of node <code>2</code>. These are the only nodes with twins for <code>n = 4</code>.</li>
</ul>

<p>The <strong>twin sum </strong>is defined as the sum of a node and its twin.</p>

<p>Given the <code>head</code> of a linked list with even length, return <em>the <strong>maximum twin sum</strong> of the linked list</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/03/eg1drawio.png" style="width: 250px; height: 70px;" />
<pre>
<strong>Input:</strong> head = [5,4,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong>
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/03/eg2drawio.png" style="width: 250px; height: 70px;" />
<pre>
<strong>Input:</strong> head = [4,2,2,3]
<strong>Output:</strong> 7
<strong>Explanation:</strong>
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
</pre>

<p><strong>Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/03/eg3drawio.png" style="width: 200px; height: 88px;" />
<pre>
<strong>Input:</strong> head = [1,100000]
<strong>Output:</strong> 100001
<strong>Explanation:</strong>
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is an <strong>even</strong> integer in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>链表</li><li>双指针</li></div></div><br><div><li>👍 5</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
var pairSum = function (head) {
  // 做法和回文字符串的做法一样 通过一次便利将内容压入栈中，再依次抛出和链表进行逐个对比。
  let dummyHead = head;
  const stack = [];
  while (dummyHead) {
    stack.push(dummyHead.val);
    dummyHead = dummyHead.next;
  }
  let curMax = head.val + stack.pop();
  head = head.next;
  while (head) {
    if (head.val + stack[stack.length - 1] > curMax) {
      curMax = head.val + stack[stack.length - 1];
    }
    stack.pop();
    head = head.next;
  }
  return curMax;
};
```

```python3
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stk1, stk2 = [], []

        # 把链表值顺序压入stk1
        while head:
            stk1.append(head.val)
            head = head.next

        # 对半分给stk2
        for _ in range(len(stk1) // 2):
            stk2.append(stk1.pop())

        # 打擂台，找到最大值
        max_ret = 0
        for _ in range(len(stk1)):
            max_ret = max(max_ret, stk1.pop() + stk2.pop())

        return max_ret

```
