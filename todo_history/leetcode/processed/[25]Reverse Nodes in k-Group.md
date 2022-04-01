<p>Given the <code>head</code> of a linked list, reverse the nodes of the list <code>k</code> at a time, and return <em>the modified list</em>.</p>

<p><code>k</code> is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of <code>k</code> then left-out nodes, in the end, should remain as it is.</p>

<p>You may not alter the values in the list&#39;s nodes, only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [2,1,4,3,5]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 3
<strong>Output:</strong> [3,2,1,4,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 5000</code></li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you solve the problem in <code>O(1)</code> extra memory space?</p>
<div><div>Related Topics</div><div><li>递归</li><li>链表</li></div></div><br><div><li>👍 1469</li><li>👎 0</li></div>

```js
var reverseKGroup = function (head, k) {
  /**
   * 思路1： 递归和循环
   * 1.1.循环：从头开始，使用几个变量存储关键节点信息，一路向下走，只不过每到k个数字，就完成一组翻转。之后重置计数
   * 如果一直到链表最后，计数没有k个，则这已经被翻转过的元素都重新翻转回来。 silly
   * 思路2: 先截取k个元素出来，之后封装一个函数 实现对这k个元素进行翻转不就行了。这种情况下明显使用正常的循环逻辑啊
   */

  // n 代表还有多少个元素需要翻转
  function reverseLinkList(node, n) {
    // 函数返回第n个元素以及n+1个元素 函数返回值不进行修改 只用来读取值
    if (n === 0) {
      return [node, node ? node.next : null];
    }
    const [nthNode, nPlus1Node] = reverseLinkList(node.next, n - 1);
    node.next.next = node;
    node.next = nPlus1Node;
    return [nthNode, nPlus1Node];
  }
  const dummyHead = new ListNode(undefined, head);
  // 得搞清楚快慢指针的物理意义 要不然就会错！！
  let fastNode = dummyHead.next;
  let slowNode = dummyHead;
  while (slowNode) {
    let i = 0;
    while (i < k) {
      // 先让快指针往前走 每满k步 执行一次reverse操作
      if (!fastNode) {
        break;
      }
      fastNode = fastNode.next;
      i += 1;
    }
    if (i < k) {
      break;
    }
    const [nthNode] = reverseLinkList(slowNode.next, k - 1);
    var temp = slowNode.next;
    slowNode.next = nthNode;
    slowNode = temp;
  }
  return dummyHead.next;
};
```