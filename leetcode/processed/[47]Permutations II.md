<p>Given a collection of numbers, <code>nums</code>,&nbsp;that might contain duplicates, return <em>all possible unique permutations <strong>in any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>回溯</li></div></div><br><div><li>👍 930</li><li>👎 0</li></div>

```js
/**
 * E.g. nums = [1,1,2]
 *                 [1,1,2]
 *                /       \
 *            1(12)       2(11)
 *          /     \         |
 *          112   12(1)     21(1)
 *                 |        |
 *                 121      211
 */

function swap(str, i, j) {
  [str[i], str[j]] = [str[j], str[i]];
}
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function (nums) {
  const result = [];
  function recursivePermutation(nums, index) {
    if (nums.length === index) {
      result.push([...nums]);
      return;
    }
    const selectedMap = new Map();
    for (let i = index; i < nums.length; i++) {
      // 每个元素只选择一次 不能重复
      if (selectedMap.has(nums[i])) {
        continue;
      }
      swap(nums, index, i);
      recursivePermutation(nums, index + 1);
      swap(nums, index, i);
      selectedMap.set(nums[i], true);
    }
  }
  recursivePermutation(nums, 0);
  return result;
};
```