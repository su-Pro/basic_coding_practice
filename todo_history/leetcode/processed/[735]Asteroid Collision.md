<p>We are given an array <code>asteroids</code> of integers representing asteroids in a row.</p>

<p>For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.</p>

<p>Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> asteroids = [5,10,-5]
<strong>Output:</strong> [5,10]
<strong>Explanation:</strong> The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> asteroids = [8,-8]
<strong>Output:</strong> []
<strong>Explanation:</strong> The 8 and -8 collide exploding each other.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> asteroids = [10,2,-5]
<strong>Output:</strong> [10]
<strong>Explanation:</strong> The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= asteroids.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= asteroids[i] &lt;= 1000</code></li>
	<li><code>asteroids[i] != 0</code></li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>数组</li></div></div><br><div><li>👍 211</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
var asteroidCollision = function (asteroids) {
  /// 稳定的 不会相撞的
  //
  /**
   * 思路整理：
   * 1. 如果当前元素大于0 则当前元素压入栈
   *
   * 如果当前元素小于0：
   * 2. 栈内顶部元素小于0 则当前元素压入栈
   * 3. 栈内顶部元素大于0  【while栈非空 栈内顶部元素大于0】
   *    3.1 栈内顶部元素 < 当前元素绝对值：栈pop元素
   *    3.2 栈内顶部元素 === 当前元素绝对值：栈pop元素 结束循环
   *    3.3 栈内顶部元素 > 当前元素绝对值：结束循环
   */
  const stack = [];
  for (let i = 0; i < asteroids.length; i++) {
    if (asteroids[i] > 0 || stack.length === 0 || stack[stack.length - 1] < 0) {
      // 1. 如果当前元素大于0 则当前元素压入栈
      // 2. 栈内顶部元素小于0 则当前元素压入栈
      stack.push(asteroids[i]);
      continue;
    }
    /** 这个地方有点恶心 得记录到底是break出来了还是最终有一个行星一路炸到了头 **/
    let breaked = false;
    // 栈内顶部元素大于0  【while栈非空 栈内顶部元素大于0】
    while (stack.length && stack[stack.length - 1] > 0) {
      if (stack[stack.length - 1] < -asteroids[i]) {
        // 3.1 栈内顶部元素 < 当前元素绝对值：栈pop元素
        stack.pop();
        continue;
      } else if (stack[stack.length - 1] === -asteroids[i]) {
        // 3.2 栈内顶部元素 === 当前元素绝对值：栈pop元素 结束循环
        stack.pop();
        breaked = true;
      }
      break;
    }
    if (!breaked) {
      // 如果是有行星一路炸到头则需要在这里push进去
      stack.push(asteroids[i]);
    }
  }
  return stack;
};
```

```python3
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            # 在当前行星前面出现过反方向的行星，需要检查到底炸谁
            while stk and asteroid < 0 < stk[-1]:
                # 一路往回炸
                if -asteroid > stk[-1]:
                    stk.pop()
                    continue
                # 两颗都炸,注意，只会有一次
                elif -asteroid == stk[-1]:
                    stk.pop()

                # 新的行星炸不了以前的(- asteroid < stk[-1])，也不能加入到stk中，手动结束循环
                break
            # 第一颗行星或者和前一个是同向
            else: stk.append(asteroid)
        return stk

```
