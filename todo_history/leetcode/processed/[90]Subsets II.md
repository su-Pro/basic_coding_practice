<p>Given an integer array <code>nums</code> that may contain duplicates, return <em>all possible subsets (the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> [[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>
<div><div>Related Topics</div><div><li>位运算</li><li>数组</li><li>回溯</li></div></div><br><div><li>👍 731</li><li>👎 0</li></div>

```js
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function (nums) {
  // **DFS基本方法：**
  // 1. what does it store on each level?
  /**
   * 首先将nums=[1,2,2,3]修改成 [<1,1>, <2,2>,<3,1>]的结构
   * 之后每个layer代表一个数，有多少个不同的数字就有多少个layer。
   */
  // 2. how many different states should we try to put on this level?
  /**
   * 每个layer中节点分别代表添加 0个当前节点、1个当前节点、2个当前节点，...
   */
  const result = [];
  function recursiveTraverse(nums, index, curCombination) {
    if (index === nums.length) {
      result.push([...curCombination]);
      return;
    }
    for (let i = 0; i <= nums[index].count; i++) {
      // 注意这里i的区间是 [0, nums[index].count] 所以循环条件得是i <= nums[index].count
      let j = 0;
      while (j < i) {
        curCombination.push(nums[index].val);
        j += 1;
      }
      recursiveTraverse(nums, index + 1, curCombination);
      while (j > 0) {
        curCombination.pop();
        j -= 1;
      }
    }
  }
  // 数组整理一下
  const numMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    numMap.set(nums[i], (numMap.get(nums[i]) || 0) + 1);
  }
  const processedNums = [...numMap.entries()].map(([key, value]) => ({
    val: key,
    count: value,
  }));
  recursiveTraverse(processedNums, 0, []);
  return result;
};
```