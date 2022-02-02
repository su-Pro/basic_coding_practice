<p>Given the <code>root</code> of a binary tree, <em>check whether it is a mirror of itself</em> (i.e., symmetric around its center).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg" style="width: 354px; height: 291px;" />
<pre>
<strong>Input:</strong> root = [1,2,2,3,4,4,3]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg" style="width: 308px; height: 258px;" />
<pre>
<strong>Input:</strong> root = [1,2,2,null,3,null,3]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it both recursively and iteratively?<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>二叉树</li></div></div><br><div><li>👍 1724</li><li>👎 0</li></div>

```js
function isSymmetric(root) {
  function traverse(leftNode, rightNode) {
    if (!leftNode && !rightNode) {
      return true;
    }
    // leftNode和rightNode两个不同时为空的情况下 有一个为空了
    // 直接用 !leftNode || !rightNode 表示即可
    if (!leftNode || !rightNode || leftNode.val !== rightNode.val) {
      return false;
    }
    return (
      traverse(leftNode.left, rightNode.right) &&
      traverse(leftNode.right, rightNode.left)
    );
  }
  return traverse(root.left, root.right);
}
/**
 * Time: O(n) 需要执行 n/2 次比较
 * Space: O(n)   O(logn) --> if tree is a balanced tree
 * ⚠️ 这里空间复杂度和树的实际结构相关
 */
```
