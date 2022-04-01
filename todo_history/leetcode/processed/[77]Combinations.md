<p>Given two integers <code>n</code> and <code>k</code>, return <em>all possible combinations of</em> <code>k</code> <em>numbers out of the range</em> <code>[1, n]</code>.</p>

<p>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4, k = 2
<strong>Output:</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> [[1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>回溯</li></div></div><br><div><li>👍 850</li><li>👎 0</li></div>

```js
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
  // **DFS基本方法：**
  // 1. what does it store on each level?
  // combination问题 采用每层代表一个值 两个分叉 分别代表选了或者是没有选 一共n层
  // 2. how many different states should we try to put on this level?
  const results = [];
  function combination(index, prefix) {
    if (prefix.length === k) {
      results.push([...prefix]);
      return;
    }
    if (index > n) {
      return;
    }
    prefix.push(index);
    combination(index + 1, prefix);
    prefix.pop();
    combination(index + 1, prefix);
  }
  combination(1, []);
  return results;
};
```