# recommend : 🌟🌟🌟🌟
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_node = ListNode()

        dummy_node.next = head

        p = dummy_node
        while p and p.next and p.next.next:
            a, b = p.next, p.next.next
            p.next = b
            a.next = b.next
            b.next = a
            p = a
        return dummy_node.next
# leetcode submit region end(Prohibit modification and deletion)
