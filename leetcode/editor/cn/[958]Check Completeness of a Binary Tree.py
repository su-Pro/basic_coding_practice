# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        que = collections.deque([root])
        flag = False
        while len(que):
            node = que.popleft()
            if node is None:
                flag = True
            else:
                if flag: return False
                que.append(node.left)
                que.append(node.right)
        return True
# leetcode submit region end(Prohibit modification and deletion)
