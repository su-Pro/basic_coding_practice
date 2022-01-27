<p>Given an integer array <code>nums</code>, return <code>true</code><em> if there exists a triple of indices </em><code>(i, j, k)</code><em> such that </em><code>i &lt; j &lt; k</code><em> and </em><code>nums[i] &lt; nums[j] &lt; nums[k]</code>. If no such indices exists, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> Any triplet where i &lt; j &lt; k is valid.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,3,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> No triplet exists.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,5,0,4,6]
<strong>Output:</strong> true
<strong>Explanation:</strong> The triplet (3, 4, 5) is valid because nums[3] == 0 &lt; nums[4] == 4 &lt; nums[5] == 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you implement a solution that runs in <code>O(n)</code> time complexity and <code>O(1)</code> space complexity?<div><div>Related Topics</div><div><li>贪心</li><li>数组</li></div></div><br><div><li>👍 452</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```python3
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = len(nums)
        l_min = [0] * l
        r_max = [0] * l
        l_min[0] = nums[0]
        r_max[l - 1] = nums[l - 1]
        # fill min value ,from left to right
        for i in range(1, l):
            l_min[i] = min(l_min[i - 1], nums[i])

        for i in range(l - 2, -1, -1):
            r_max[i] = max(r_max[i + 1], nums[i])

        for i in range(1, l - 1):
            if l_min[i - 1] < nums[i] < r_max[i + 1]: return True
        return False



```
  