# Design a max stack data structure that supports the stack operations and 
# supports finding the stack's maximum element. 
# 
#  Implement the MaxStack class: 
# 
#  
#  MaxStack() Initializes the stack object. 
#  void push(int x) Pushes element x onto the stack. 
#  int pop() Removes the element on top of the stack and returns it. 
#  int top() Gets the element on the top of the stack without removing it. 
#  int peekMax() Retrieves the maximum element in the stack without removing it.
#  
#  int popMax() Retrieves the maximum element in the stack and removes it. If 
# there is more than one maximum element, only remove the top-most one. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop",
#  "top"]
# [[], [5], [1], [5], [], [], [], [], [], []]
# Output
# [null, null, null, null, 5, 5, 1, 5, 1, 5]
# 
# Explanation
# MaxStack stk = new MaxStack();
# stk.push(5);   // [5] the top of the stack and the maximum number is 5.
# stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
# stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the 
# maximum, because it is the top most one.
# stk.top();     // return 5, [5, 1, 5] the stack did not change.
# stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is 
# different from the max.
# stk.top();     // return 1, [5, 1] the stack did not change.
# stk.peekMax(); // return 5, [5, 1] the stack did not change.
# stk.pop();     // return 1, [5] the top of the stack and the max element is 
# now 5.
# stk.top();     // return 5, [5] the stack did not change.
#  
# 
#  
#  Constraints: 
# 
#  
#  -10⁷ <= x <= 10⁷ 
#  At most 10⁴ calls will be made to push, pop, top, peekMax, and popMax. 
#  There will be at least one element in the stack when pop, top, peekMax, or 
# popMax is called. 
#  
# 
#  
# Follow up: Could you come up with a solution that supports O(1) for each top 
# call and O(logn) for each other call? Related Topics 栈 设计 链表 双向链表 有序集合 👍 90 👎 0
# 


# leetcode submit region begin(Prohibit modification and deletion)
class MaxStack:

    def __init__(self):
        self.stk = []
        self.stk_max = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        cnt = 0
        while len(self.stk_max) and x < self.stk_max[-1]:
            self.stk.append(self.stk_max.pop())
            cnt += 1

        self.stk_max.append(x)

        while cnt != 0:
            self.stk_max.append(self.stk.pop())
            cnt -= 1

    def pop(self) -> int:
        v = self.stk.pop()
        cnt = 0
        while len(self.stk_max) and v < self.stk_max[-1]:
            self.stk.append(self.stk_max.pop())
            cnt += 1

        self.stk_max.pop()

        while cnt != 0:
            self.stk_max.append(self.stk.pop())
            cnt -= 1
        return v

    def top(self) -> int:
        return self.stk[-1]

    def peekMax(self) -> int:
        return self.stk_max[-1]

    def popMax(self) -> int:
        # 同步减
        top_max = self.stk_max.pop()
        cnt = 0
        while self.stk[-1] != top_max:
            self.stk_max.append(self.stk.pop())
            cnt += 1
        # 同步减
        self.stk.pop()
        while cnt != 0:
            self.stk.append(self.stk_max.pop())
            cnt -= 1
        print(self.stk, self.stk_max)
        return top_max
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
# leetcode submit region end(Prohibit modification and deletion)
