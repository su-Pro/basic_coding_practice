<p>A <a href="https://en.wikipedia.org/wiki/Trie" target="_blank"><strong>trie</strong></a> (pronounced as &quot;try&quot;) or <strong>prefix tree</strong> is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.</p>

<p>Implement the Trie class:</p>

<ul>
	<li><code>Trie()</code> Initializes the trie object.</li>
	<li><code>void insert(String word)</code> Inserts the string <code>word</code> into the trie.</li>
	<li><code>boolean search(String word)</code> Returns <code>true</code> if the string <code>word</code> is in the trie (i.e., was inserted before), and <code>false</code> otherwise.</li>
	<li><code>boolean startsWith(String prefix)</code> Returns <code>true</code> if there is a previously inserted string <code>word</code> that has the prefix <code>prefix</code>, and <code>false</code> otherwise.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Trie&quot;, &quot;insert&quot;, &quot;search&quot;, &quot;search&quot;, &quot;startsWith&quot;, &quot;insert&quot;, &quot;search&quot;]
[[], [&quot;apple&quot;], [&quot;apple&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;]]
<strong>Output</strong>
[null, null, true, false, true, null, true]

<strong>Explanation</strong>
Trie trie = new Trie();
trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // return True
trie.search(&quot;app&quot;);     // return False
trie.startsWith(&quot;app&quot;); // return True
trie.insert(&quot;app&quot;);
trie.search(&quot;app&quot;);     // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
	<li><code>word</code> and <code>prefix</code> consist only of lowercase English letters.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls <strong>in total</strong> will be made to <code>insert</code>, <code>search</code>, and <code>startsWith</code>.</li>
</ul>
<div><div>Related Topics</div><div><li>设计</li><li>字典树</li><li>哈希表</li><li>字符串</li></div></div><br><div><li>👍 1026</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```python3
class Trie:

    def __init__(self):
        # 这里的N是一次性初始化的容量
        self.N = 100009
        self.son_set = [[0] * 26 for i in range(self.N)]
        self.cnt = [0] * self.N
        #标识当前已经有几个节点进入了Trie中
        self.idx = 0

    def insert(self, word: str) -> None:
        p_idx = 0
        for _, ch in enumerate(word):
            ch_u = ord(ch) - ord('a')
            if self.son_set[p_idx][ch_u] is 0:
                self.idx += 1
                self.son_set[p_idx][ch_u] = self.idx
            p_idx = self.son_set[p_idx][ch_u]
        self.cnt[p_idx] += 1

    def search(self, word: str) -> bool:
        p_idx = 0
        for _, ch in enumerate(word):
            ch_u = ord(ch) - ord('a')
            if self.son_set[p_idx][ch_u] is 0: return False
            p_idx = self.son_set[p_idx][ch_u]
        return self.cnt[p_idx] != 0

    def startsWith(self, prefix: str) -> bool:
        p_idx = 0
        for _,ch in enumerate(prefix):
            ch_u = ord(ch) - ord('a')
            if self.son_set[p_idx][ch_u] is 0: return False
            p_idx = self.son_set[p_idx][ch_u]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

```
  