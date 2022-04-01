<p>Given an array of integers <code>nums</code>, sort the array in ascending order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,2,3,1]
<strong>Output:</strong> [1,2,3,5]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,1,1,2,0,0]
<strong>Output:</strong> [0,0,1,1,2,5]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-5 * 10<sup>4</sup> &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>分治</li><li>桶排序</li><li>计数排序</li><li>基数排序</li><li>排序</li><li>堆（优先队列）</li><li>归并排序</li></div></div><br><div><li>👍 468</li><li>👎 0</li></div>
<strong> solution: </strong>

```js
/**
 * 选择排序
 * 每次迭代 选择最小的放到前面。
 */
function selectionSort(nums) {
  // how many iterations
  for (let i = 0; i < nums.length - 1; i++) {
    let curMinIndex = i;
    // find the global min from the rest elements
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] < nums[curMinIndex]) {
        curMinIndex = j;
      }
    }
    [nums[curMinIndex], nums[i]] = [nums[i], nums[curMinIndex]];
  }
  return nums;
}
/**
Complexity
  Time O(n^2)
  n elements to check, n - 1 elements to compare and find the current min in each iteration →
  in total, there are n, n - 1, n - 2, ... , 2, 1 operations → n * (n+1) / 2 → O(n^2)

  Space O(1)
 */

// 注意boundary 以及iteration times
// TODO: given an array sorted in stask1, how to sort the numbers by using additional two stasks?

/** --------------------------------------------------------------------- */
/**
 * Merge Sort 归并排序
 * 先拆分 后治理的策略
 */
function mergeSortArray(nums) {
  function mergeSort(nums, left, right) {
    if (left >= right) {
      return [nums[left]];
    }
    let mid = Math.floor((right + left) / 2);
    const solu_left = mergeSort(nums, left, mid);
    const solu_right = mergeSort(nums, mid + 1, right);
    return mergeArray(solu_left, solu_right);
  }
  function mergeArray(arr1, arr2) {
    let i = 0,
      j = 0;
    const result = [];
    while (i < arr1.length || j < arr2.length) {
      if (j === arr2.length || arr1[i] < arr2[j]) {
        result.push(arr1[i]);
        i += 1;
      } else {
        result.push(arr2[j]);
        j += 1;
      }
      // 错误版本 在修改完了i之后 并没有走else 以为判断条件互不干扰
      // 但条件判断中有副作用了 不能想当然
      // if (j === arr2.length || arr1[i] < arr2[j]) {
      //   result.push(arr1[i]);
      //   i += 1;
      // }
      // if (i === arr1.length || arr1[i] >= arr2[j]) {
      //   result.push(arr2[j]);
      //   j += 1;
      // }
    }
    return result;
  }
  return mergeSort(nums, 0, nums.length - 1);
}
/**
  Complexity  Time nlog(n) Space O(n)
*/
/** --------------------------------------------------------------------- */

/**
 * 快速排序
 * 我们可以随便选一个元素，假如我们选数组的最后一个元素，我们把这个元素称之为”主元“吧。
 * 然后将大于或等于主元的元素放在右边，把小于或等于主元的元素放在左边。
 * 此时主元所处的位置，是一个有序的位置,即主元已经处于排好序的位置了。
 *
 * 主元把数组分成了两半部分。把一个大的数组通过主元分割成两小部分的这个操作，我们也称之为分割操作(partition)
 *
 * 快速排序有两种分割操作：单向调整、双向调整
 */

// 单向调整
//leetcode submit region begin(Prohibit modification and deletion)
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function quickSortFn(nums) {
  function quickSort(nums, left, right) {
    // pivot = right;
    // 如果pivot选择在了最后面 则单向调整得从第一个元素开始调整了。
    // 反之，如果pivot选择第一个元素 则单向调整得从最后一个元素向前开始调整。就比较麻烦。
    if (left >= right) {
      // 注意这里是大于等于
      return;
    }
    let pivotMinusOneIndex = left;
    for (let i = left; i <= right - 1; i++) {
      if (nums[i] < nums[right]) {
        // 这里仅仅需要swap就可以了
        [nums[pivotMinusOneIndex], nums[i]] = [
          nums[i],
          nums[pivotMinusOneIndex],
        ];
        pivotMinusOneIndex += 1;
      }
    }
    [nums[pivotMinusOneIndex], nums[right]] = [
      nums[right],
      nums[pivotMinusOneIndex],
    ];
    // 这里注意boundary啊 是 pivotMinusOneIndex-1 而不是 pivotMinusOneIndex
    quickSort(nums, left, pivotMinusOneIndex - 1); // left half
    quickSort(nums, pivotMinusOneIndex + 1, right); // right half
  }
  quickSort(nums, 0, nums.length - 1);
  return nums;
};
//leetcode submit region end(Prohibit modification and deletion)
/**
  Complexity  Time nlog(n) Space O(n)
*/
```
