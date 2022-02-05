<p>Given a string <code>s</code>, you&nbsp;can transform every letter individually to be lowercase or uppercase to create another string.</p>

<p>Return <em>a list of all possible strings we could create</em>. Return the output in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a1b2&quot;
<strong>Output:</strong> [&quot;a1b2&quot;,&quot;a1B2&quot;,&quot;A1b2&quot;,&quot;A1B2&quot;]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;3z4&quot;
<strong>Output:</strong> [&quot;3z4&quot;,&quot;3Z4&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 12</code></li>
	<li><code>s</code> consists of lowercase English letters, uppercase English letters, and digits.</li>
</ul>
<div><div>Related Topics</div><div><li>位运算</li><li>字符串</li><li>回溯</li></div></div><br><div><li>👍 354</li><li>👎 0</li></div>

```js
function replaceAt(str, index, replacement) {
  return (
    str.substr(0, index) + replacement + str.substr(index + replacement.length)
  );
}
/**
 * @param {string} s
 * @return {string[]}
 */
var letterCasePermutation = function (s) {
  // 首先得理解 这个是个排列问题 因为"a1B2"和"A1b2"是两个不同的结果
  const results = [];
  function permutation(input, index) {
    if (input.length === index) {
      results.push(input + "");
      return;
    }
    if (!Number.isNaN(Number(input[index]))) {
      permutation(input, index + 1);
    } else {
      permutation(
        replaceAt(input, index, input[index].toLowerCase()),
        index + 1
      );
      permutation(
        replaceAt(input, index, input[index].toUpperCase()),
        index + 1
      );
    }
  }
  permutation(s, 0);
  return results;
};
```