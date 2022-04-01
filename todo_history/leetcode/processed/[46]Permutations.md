<p>Given an array <code>nums</code> of distinct integers, return <em>all the possible permutations</em>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [[0,1],[1,0]]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 6</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>回溯</li></div></div><br><div><li>👍 1752</li><li>👎 0</li></div>

```js
function swap(str, i, j) {
  [str[i], str[j]] = [str[j], str[i]];
}
/**
 * string = 'abc'
 * E.g 'abc'
 *     'acb'
 *     'bac'
 *     ...
 *
 *                              root = 'abc'
 *                      /             |               \
 * level1         a(bc)             b(ac)             c(ab)
 *                /   \             /    \             /     \
 * level2     b(c)   c(b)        a(c)    c(a)         a(b)   b(a)
 *             |      |            |      |            |       |
 * level3      c      b           c      a             b       a
 *
 * Time = O(n!)
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
  const result = [];
  function permutation(nums, index) {
    if (index === nums.length) {
      result.push([...nums]);
      return;
    }
    // 清楚 这里从第几个索引初开始遍历 并且遍历到哪个节点
    for (let i = index; i < nums.length; i++) {
      swap(nums, index, i);
      permutation(nums, index + 1);
      swap(nums, index, i);
    }
  }
  permutation(nums, 0);
  return result;
};
```
```python3
class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     ret, l_input = [], len(nums)
    #
    #     def dfs(level: int):
    #         if level == l_input:
    #             ret.append(nums[:])
    #             return
    #
    #         for i in range(level, l_input):
    #             nums[level], nums[i] = nums[i], nums[level]
    #             dfs(level + 1)
    #             nums[level], nums[i] = nums[i], nums[level]
    #
    #     dfs(0)
    #     return ret

    # 更通用的DFS做法
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret, l_input, visted = [], len(nums) + 1, dict((v, False) for v in nums)

        def dfs(level: int, path: List[int]):
            if level is l_input:
                ret.append(path.copy())
                return

            for v in visted:
                if visted[v]: continue

                path.append(v)
                visted[v] = True

                dfs(level + 1, path)

                path.pop()
                visted[v] = False

        dfs(1, [])
        return ret

```