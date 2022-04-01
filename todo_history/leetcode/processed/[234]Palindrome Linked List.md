<p>Given the <code>head</code> of a singly linked list, return <code>true</code> if it is a palindrome.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2,2,1]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
<pre>
<strong>Input:</strong> head = [1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do it in <code>O(n)</code> time and <code>O(1)</code> space?<div><div>Related Topics</div><div><li>栈</li><li>递归</li><li>链表</li><li>双指针</li></div></div><br><div><li>👍 1247</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
var isPalindrome = function (head) {
  // 这个函数如果是判断一个string是不是回文字符串 那么从中间开始往两边用两个指针不断移动，并且
  // 相互比较值的大小就行了
  // 链表如果要比较就从第一个元素和最后一个元素开始比对
  // 如果将链表值全部copy至stack 那么之后再一个一个pop 就可以将链表从后往前迭代了。

  const stack = new Stack();
  // 由于我们不想要修改head的指向 因此我们新建一个节点 之后对链表进行遍历
  let dummyHead = head;
  while (dummyHead) {
    stack.push(dummyHead.val);
    dummyHead = dummyHead.next;
  }
  while (head.next) {
    if (head.val !== stack.peek()) {
      return false;
    }
    stack.pop();
    head = head.next;
  }
  return true;
};
```

```python3
class Solution:
    # O(n) 空间做法，利用stack来模拟递归逻辑
    def isPalindrome(self, head: ListNode) -> bool:
        stk, dummy_head = [], ListNode()

        dummy_head.next = head  # 构造dummy_head，用于遍历链表
        dummy_head = dummy_head.next

        while dummy_head:
            stk.append(dummy_head)
            dummy_head = dummy_head.next

        while stk:
            if head.val != stk[-1].val: return False
            # 向前一步，向后一步
            stk.pop()
            head = head.next

        return True

```
