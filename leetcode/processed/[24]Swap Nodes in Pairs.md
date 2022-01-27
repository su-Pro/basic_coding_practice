<p>Given a&nbsp;linked list, swap every two adjacent nodes and return its head. You must solve the problem without&nbsp;modifying the values in the list&#39;s nodes (i.e., only nodes themselves may be changed.)</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [2,1,4,3]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the&nbsp;list&nbsp;is in the range <code>[0, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
</ul>
<div><div>Related Topics</div><div><li>递归</li><li>链表</li></div></div><br><div><li>👍 1212</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```python3
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_node = ListNode()

        dummy_node.next = head

        p = dummy_node
        while p and p.next and p.next.next:
            a, b = p.next, p.next.next
            p.next = b
            a.next = b.next
            b.next = a
            p = a
        return dummy_node.next

```
  