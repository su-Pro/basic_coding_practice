<p>Given the <code>root</code> of a binary tree, return <em>all root-to-leaf paths in <strong>any order</strong></em>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" style="width: 207px; height: 293px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,5]
<strong>Output:</strong> [&quot;1-&gt;2-&gt;5&quot;,&quot;1-&gt;3&quot;]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [&quot;1&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>字符串</li><li>回溯</li><li>二叉树</li></div></div><br><div><li>👍 641</li><li>👎 0</li></div>

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function (root) {
  // 直接preorder traverse二叉树即可
  const results = [];
  if (!root) {
    return [];
  }
  function traverse(node, result) {
    /**
     * 两边子节点 均为空时 算一条路径
     * keypoint⚠️: 每层循环中 必须得push一次 对应的也pop一次。
     * 因此这里有两处地方需要pop 在提前return时 别忘了也得pop一次。
     */
    result.push(node.val);
    if (!node.left && !node.right) {
      results.push(result.join("->"));
      result.pop();
      return;
    }
    if (node.left) {
      traverse(node.left, result);
    }
    if (node.right) {
      traverse(node.right, result);
    }
    result.pop();
  }
  traverse(root, []);
  return results;
};
```