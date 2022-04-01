<p>You have a <strong>browser</strong> of one tab where you start on the <code>homepage</code> and you can visit another <code>url</code>, get back in the history number of <code>steps</code> or move forward in the history number of <code>steps</code>.</p>

<p>Implement the <code>BrowserHistory</code> class:</p>

<ul>
	<li><code>BrowserHistory(string homepage)</code> Initializes the object with the <code>homepage</code>&nbsp;of the browser.</li>
	<li><code>void visit(string url)</code>&nbsp;Visits&nbsp;<code>url</code> from the current page. It clears up all the forward history.</li>
	<li><code>string back(int steps)</code>&nbsp;Move <code>steps</code> back in history. If you can only return <code>x</code> steps in the history and <code>steps &gt; x</code>, you will&nbsp;return only <code>x</code> steps. Return the current <code>url</code>&nbsp;after moving back in history <strong>at most</strong> <code>steps</code>.</li>
	<li><code>string forward(int steps)</code>&nbsp;Move <code>steps</code> forward in history. If you can only forward <code>x</code> steps in the history and <code>steps &gt; x</code>, you will&nbsp;forward only&nbsp;<code>x</code> steps. Return the current <code>url</code>&nbsp;after forwarding in history <strong>at most</strong> <code>steps</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example:</strong></p>

<pre>
<b>Input:</b>
[&quot;BrowserHistory&quot;,&quot;visit&quot;,&quot;visit&quot;,&quot;visit&quot;,&quot;back&quot;,&quot;back&quot;,&quot;forward&quot;,&quot;visit&quot;,&quot;forward&quot;,&quot;back&quot;,&quot;back&quot;]
[[&quot;leetcode.com&quot;],[&quot;google.com&quot;],[&quot;facebook.com&quot;],[&quot;youtube.com&quot;],[1],[1],[1],[&quot;linkedin.com&quot;],[2],[2],[7]]
<b>Output:</b>
[null,null,null,null,&quot;facebook.com&quot;,&quot;google.com&quot;,&quot;facebook.com&quot;,null,&quot;linkedin.com&quot;,&quot;google.com&quot;,&quot;leetcode.com&quot;]

<b>Explanation:</b>
BrowserHistory browserHistory = new BrowserHistory(&quot;leetcode.com&quot;);
browserHistory.visit(&quot;google.com&quot;);       // You are in &quot;leetcode.com&quot;. Visit &quot;google.com&quot;
browserHistory.visit(&quot;facebook.com&quot;);     // You are in &quot;google.com&quot;. Visit &quot;facebook.com&quot;
browserHistory.visit(&quot;youtube.com&quot;);      // You are in &quot;facebook.com&quot;. Visit &quot;youtube.com&quot;
browserHistory.back(1);                   // You are in &quot;youtube.com&quot;, move back to &quot;facebook.com&quot; return &quot;facebook.com&quot;
browserHistory.back(1);                   // You are in &quot;facebook.com&quot;, move back to &quot;google.com&quot; return &quot;google.com&quot;
browserHistory.forward(1);                // You are in &quot;google.com&quot;, move forward to &quot;facebook.com&quot; return &quot;facebook.com&quot;
browserHistory.visit(&quot;linkedin.com&quot;);     // You are in &quot;facebook.com&quot;. Visit &quot;linkedin.com&quot;
browserHistory.forward(2);                // You are in &quot;linkedin.com&quot;, you cannot move forward any steps.
browserHistory.back(2);                   // You are in &quot;linkedin.com&quot;, move back two steps to &quot;facebook.com&quot; then to &quot;google.com&quot;. return &quot;google.com&quot;
browserHistory.back(7);                   // You are in &quot;google.com&quot;, you can move back only one step to &quot;leetcode.com&quot;. return &quot;leetcode.com&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= homepage.length &lt;= 20</code></li>
	<li><code>1 &lt;= url.length &lt;= 20</code></li>
	<li><code>1 &lt;= steps &lt;= 100</code></li>
	<li><code>homepage</code> and <code>url</code> consist of&nbsp; &#39;.&#39; or lower case English letters.</li>
	<li>At most <code>5000</code>&nbsp;calls will be made to <code>visit</code>, <code>back</code>, and <code>forward</code>.</li>
</ul>
<div><div>Related Topics</div><div><li>栈</li><li>设计</li><li>数组</li><li>链表</li><li>数据流</li><li>双向链表</li></div></div><br><div><li>👍 42</li><li>👎 0</li></div> 
<br>
<strong> solution: </strong>

```javascript
/**
 * @param {string} homepage
 */
class BrowserHistory {
  constructor(homepage) {
    this.backStack = new Stack();
    this.forwardStack = new Stack();
    this.backStack.push(homepage);
  }
  /**
   * @param {string} url
   * @return {void}
   */
  visit(url) {
    while (!this.forwardStack.isEmpty()) {
      this.forwardStack.pop();
    }
    this.backStack.push(url);
  }
  /**
   * @param {number} steps
   * @return {string}
   */
  back(steps) {
    for (let i = 0; i < steps; i++) {
      if (this.backStack.length() === 1) {
        return this.backStack.peek();
      }
      this.forwardStack.push(this.backStack.pop());
    }
    return this.backStack.peek();
  }
  /**
   * @param {number} steps
   * @return {string}
   */
  forward(steps) {
    for (let i = 0; i < steps; i++) {
      if (this.forwardStack.isEmpty()) {
        break;
      }
      this.backStack.push(this.forwardStack.pop());
    }
    return this.backStack.peek();
  }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
```

```python3
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stk_cur = [homepage]
        self.stk_f = []

    def visit(self, url: str) -> None:
        self.stk_cur.append(url)
        self.stk_f.clear()

    def back(self, steps: int) -> str:
        stk_cur = self.stk_cur
        stk_f = self.stk_f

        while steps > 0 and len(stk_cur) > 1:
            stk_f.append(stk_cur.pop())
            steps -= 1
        return stk_cur[-1]

    def forward(self, steps: int) -> str:
        stk_cur = self.stk_cur
        stk_f = self.stk_f

        while steps > 0 and len(stk_f) > 0:
            stk_cur.append(stk_f.pop())
            steps -= 1
        return stk_cur[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

```
