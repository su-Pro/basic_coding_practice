<p>Given an integer <code>n</code>, return <em>the number of structurally unique <strong>BST&#39;</strong>s (binary search trees) which has exactly </em><code>n</code><em> nodes of unique values from</em> <code>1</code> <em>to</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 5
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 19</code></li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>二叉搜索树</li><li>数学</li><li>动态规划</li><li>二叉树</li></div></div><br><div><li>👍 1544</li><li>👎 0</li></div>

```js
/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function (n) {
  /**
   * 举个例子，比如给算法输入n = 5，也就是说用{1,2,3,4,5}这些数字去构造 BST。
   * 首先，这棵 BST 的根节点总共有几种情况？  5种情况
   * 如果固定3作为根节点，左子树节点就是{1,2}的组合，右子树就是{4,5}的组合。
   *
   * **左子树的组合数和右子树的组合数乘积** 就是3作为根节点时的BST个数
   * 因此这道题目递归解法中有一个 left 一个 right 代表窗口大小
   *
   * base case是left > right （为啥不是 == 呢？ 是因为切窗口时 我们先选择一个节点 然后以这个点为切点取左右边）
   * recursive rule很重要 就是左边函数返回值乘以右边函数返回值
   *
   * 时间复杂度非常高，肯定存在重叠子问题 因此可以定义一个map来记录重复计算的值
   */
  /**
   * 这个题目其实和建立二叉树没有关系，和DFS也没有多少关系
   * 重点在于： 1.了解二叉树的基本性质  2.能不能想到将复杂问题化解成简单问题
   */
  const memo = {};
  function recurse(left, right) {
    if (left > right) {
      return 1;
    }
    if (memo[`${left}-${right}`] !== undefined) {
      return memo[`${left}-${right}`];
    }
    let res = 0;
    for (let i = left; i <= right; i++) {
      const resl = recurse(left, i - 1); // 注意这里切窗口时 不能把i本身包含进去
      const resr = recurse(i + 1, right);
      res += resl * resr;
    }
    memo[`${left}-${right}`] = res;
    return res;
  }
  return recurse(1, n);
};
```
