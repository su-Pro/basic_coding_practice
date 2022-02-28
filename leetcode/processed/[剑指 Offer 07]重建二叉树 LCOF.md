<p>English description is not available for the problem. Please switch to Chinese.</p><div><div>Related Topics</div><div><li>树</li><li>数组</li><li>哈希表</li><li>分治</li><li>二叉树</li></div></div><br><div><li>👍 660</li><li>👎 0</li></div>

```js
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  /**
   * 这道题需要观察数组中的顺序，就是找到它的规律问题。
   * 解决这种问题时，答案肯定不是很明显的，需要画图去帮助查找规律。
   *                   3
   *            9             20
   *     11        6     15       7
   *       13
   * Preorder: [3,9,11,13,6,20,15,7]
   * Inorder: [11,13,9,6,3,15,20,7]
   * 首先通过Preorder我们知道3肯定是跟节点。因此构建二叉树的起点应该也是从遍历Preorder的每个节点开始更合理一些。
   * 其次我们发现在Preorder中：
   *    所有第i+1个节点元素 是第i个元素的要么左节点要么是右节点 或者是某父亲节点的右节点
   * 另外在Inorder中：
   *    第i节点之前的元素是第i节点的左子树上的节点或是某父亲节点
   *    第i节点之后的元素是第i节点的右节点或是父亲节点 或者是某父亲节点的右节点
   *
   *
   * 发现上面的思路不对 上面的思路解不出来问题！！ 重来
   * 前序遍历性质： 节点按照 [ 根节点 | 左子树 | 右子树 ] 排序。
   * 中序遍历性质： 节点按照 [ 左子树 | 根节点 | 右子树 ] 排序。
   * 根据以上性质，可得出以下推论：
   * 1.前序遍历的首元素 为 树的根节点 node 的值。
   * 2.在中序遍历中搜索根节点 node 的索引 ，可将 中序遍历 划分为 [ 左子树 | 根节点 | 右子树 ] 。
   * 3.根据中序遍历中的左（右）子树的节点数量，可将 前序遍历 划分为 [ 根节点 | 左子树 | 右子树 ] 。
   * https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/mian-shi-ti-07-zhong-jian-er-cha-shu-di-gui-fa-qin/
   * 通过以上三步，可确定 三个节点 ：1.树的根节点、2.左子树根节点、3.右子树根节点。
   * 根据「分治算法」思想，对于树的左、右子树，仍可复用以上方法划分子树的左右子树。
   *
   * 11, 13, 9, 6, 3, 15, 20, 7
   * L             T          L
   * 需要维护的变量有三个 其中T的位置的选取完全是根据Preorder中元素的来计算出来的。
   * 这道题逻辑比较复杂 想清楚才能做出来
   *
   */
  if (preorder.length === 0) {
    return null;
  }
  const Tree = new TreeNode(preorder[0]);
  const InorderIndexMap = new Map(inorder.map((item, index) => [item, index]));
  /** index是preOrder中当前元素的索引 leftIndex是Inorder中左边边界 rightIndex是Inorder中右边边界 */
  /**
   * 理解leftIndex, rightIndex的作用至关重要 我们窗口的定义是在中序遍历上的一颗树的边界
   * 我们不需要记录preOrder中任何东西 只要我们知道了当前节点一共有多少个左子树和多少个右子树
   * preOrder中就可以找到当前节点的左右子节点
   */
  function buildTreeRecursive(node, index, leftIndex, rightIndex) {
    if (leftIndex === rightIndex) {
      return;
    }
    const curNodeInInorderIndex = InorderIndexMap.get(preorder[index]);
    const leftNodeNums = curNodeInInorderIndex - leftIndex;
    const rightNodeNums = rightIndex - curNodeInInorderIndex;
    if (leftNodeNums > 0) {
      node.left = new TreeNode(preorder[index + 1]);
      buildTreeRecursive(
        node.left,
        index + 1,
        leftIndex,
        curNodeInInorderIndex - 1
      );
    }
    if (rightNodeNums > 0) {
      node.right = new TreeNode(preorder[index + leftNodeNums + 1]);
      buildTreeRecursive(
        node.right,
        index + leftNodeNums + 1,
        curNodeInInorderIndex + 1,
        rightIndex
      );
    }
  }
  buildTreeRecursive(Tree, 0, 0, preorder.length - 1);
  return Tree;
};
```
