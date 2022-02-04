<p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible subsets (the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>
<div><div>Related Topics</div><div><li>位运算</li><li>数组</li><li>回溯</li></div></div><br><div><li>👍 1467</li><li>👎 0</li></div>

```js
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  // **DFS基本方法：**
  // 1. what does it store on each level?
  // 一共有nums.length个layer 典型的subset问题 每个layer两个节点 分别表示加或者不加入当前节点
  // 2. how many different states should we try to put on this level?
  const results = [];
  function recursiveTraverse(nums, index, curCombination) {
    if (nums.length === index) {
      // 这里对数组进行一个拷贝 不然这个引用值会被recursion函数修改掉
      results.push([...curCombination]);
      return;
    }
    curCombination.push(nums[index]);
    recursiveTraverse(nums, index + 1, curCombination);
    curCombination.pop();
    recursiveTraverse(nums, index + 1, curCombination);
  }
  recursiveTraverse(nums, 0, []);
  return results;
};
```