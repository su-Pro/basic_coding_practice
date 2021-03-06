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
<div><div>Related Topics</div><div><li>æ </li><li>æ°ç»</li></div></div><br><div><li>ð 211</li><li>ð 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
var asteroidCollision = function (asteroids) {
  /// ç¨³å®ç ä¸ä¼ç¸æç
  //
  /**
   * æè·¯æ´çï¼
   * 1. å¦æå½ååç´ å¤§äº0 åå½ååç´ åå¥æ 
   *
   * å¦æå½ååç´ å°äº0ï¼
   * 2. æ åé¡¶é¨åç´ å°äº0 åå½ååç´ åå¥æ 
   * 3. æ åé¡¶é¨åç´ å¤§äº0  ãwhileæ éç©º æ åé¡¶é¨åç´ å¤§äº0ã
   *    3.1 æ åé¡¶é¨åç´  < å½ååç´ ç»å¯¹å¼ï¼æ popåç´ 
   *    3.2 æ åé¡¶é¨åç´  === å½ååç´ ç»å¯¹å¼ï¼æ popåç´  ç»æå¾ªç¯
   *    3.3 æ åé¡¶é¨åç´  > å½ååç´ ç»å¯¹å¼ï¼ç»æå¾ªç¯
   */
  const stack = [];
  for (let i = 0; i < asteroids.length; i++) {
    if (asteroids[i] > 0 || stack.length === 0 || stack[stack.length - 1] < 0) {
      // 1. å¦æå½ååç´ å¤§äº0 åå½ååç´ åå¥æ 
      // 2. æ åé¡¶é¨åç´ å°äº0 åå½ååç´ åå¥æ 
      stack.push(asteroids[i]);
      continue;
    }
    /** è¿ä¸ªå°æ¹æç¹æ¶å¿ å¾è®°å½å°åºæ¯breakåºæ¥äºè¿æ¯æç»æä¸ä¸ªè¡æä¸è·¯ç¸å°äºå¤´ **/
    let breaked = false;
    // æ åé¡¶é¨åç´ å¤§äº0  ãwhileæ éç©º æ åé¡¶é¨åç´ å¤§äº0ã
    while (stack.length && stack[stack.length - 1] > 0) {
      if (stack[stack.length - 1] < -asteroids[i]) {
        // 3.1 æ åé¡¶é¨åç´  < å½ååç´ ç»å¯¹å¼ï¼æ popåç´ 
        stack.pop();
        continue;
      } else if (stack[stack.length - 1] === -asteroids[i]) {
        // 3.2 æ åé¡¶é¨åç´  === å½ååç´ ç»å¯¹å¼ï¼æ popåç´  ç»æå¾ªç¯
        stack.pop();
        breaked = true;
      }
      break;
    }
    if (!breaked) {
      // å¦ææ¯æè¡æä¸è·¯ç¸å°å¤´åéè¦å¨è¿épushè¿å»
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
            # å¨å½åè¡æåé¢åºç°è¿åæ¹åçè¡æï¼éè¦æ£æ¥å°åºç¸è°
            while stk and asteroid < 0 < stk[-1]:
                # ä¸è·¯å¾åç¸
                if -asteroid > stk[-1]:
                    stk.pop()
                    continue
                # ä¸¤é¢é½ç¸,æ³¨æï¼åªä¼æä¸æ¬¡
                elif -asteroid == stk[-1]:
                    stk.pop()

                # æ°çè¡æç¸ä¸äºä»¥åç(- asteroid < stk[-1])ï¼ä¹ä¸è½å å¥å°stkä¸­ï¼æå¨ç»æå¾ªç¯
                break
            # ç¬¬ä¸é¢è¡ææèååä¸ä¸ªæ¯åå
            else: stk.append(asteroid)
        return stk

```
