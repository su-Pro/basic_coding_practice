<p>Given a string <code>s</code>, remove duplicate letters so that every letter appears once and only once. You must make sure your result is <strong>the smallest in lexicographical order</strong> among all possible results.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bcabc&quot;
<strong>Output:</strong> &quot;abc&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbacdcbc&quot;
<strong>Output:</strong> &quot;acdb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1081: <a href="https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/" target="_blank">https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/</a></p>
<div><div>Related Topics</div><div><li>栈</li><li>贪心</li><li>字符串</li><li>单调栈</li></div></div><br><div><li>👍 643</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```python3
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        visted = set()
        cntDict = collections.Counter(s)
        print(cntDict)
        for ch in s:
            # 如果已经检查存在栈中，则接续
            if ch in visted:
                cntDict[ch] -= 1
                continue

            while len(stk):
                t = stk[-1]
                if ord(ch) >= ord(t) or cntDict[t] <= 1: break
                cntDict[t] -= 1
                visted.remove(t)
                stk.pop()
            visted.add(ch)
            stk.append(ch)
        return ''.join(stk)

s = Solution()

s.removeDuplicateLetters('abcabc')

```
  