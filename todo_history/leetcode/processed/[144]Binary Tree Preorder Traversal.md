<p>Given the <code>root</code> of a binary tree, return <em>the preorder traversal of its nodes&#39; values</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 125px; height: 200px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>
<div><div>Related Topics</div><div><li>栈</li><li>树</li><li>深度优先搜索</li><li>二叉树</li></div></div><br><div><li>👍 723</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
var preorderTraversal = function (root) {
  // 递归解
  const res = [];
  function preorder(node) {
    if (!node) {
      return;
    }
    res.push(node.val);
    preorder(node.left);
    preorder(node.right);
  }
  preorder(root);
  return res;
};

var preorderTraversal = function (root) {
  if (!root) {
    return [];
  }
  /**
   * 迭代写法 迭代写法和递归写法中的调用栈不能一样，因为迭代总是在同一个代码块中执行。
   */
  // 这个代码报错 本地调试没有问题不知道问题出在哪
  const res = [];
  const stack = [];
  stack.push(root);
  while (stack.length) {
    const top = stack.pop();
    res.push(top.val);
    if (top.left) {
      stack.push(top.left);
      continue;
    }
    if (top.right) {
      stack.push(top.right);
      continue;
    }
  }
  return res;
};
```

```python3
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ret, stk = [], [root]

        while stk:
            root = stk.pop()
            if root.right: stk.append(root.right)
            if root.left: stk.append(root.left)

            ret.append(root.val)

        return ret

```
