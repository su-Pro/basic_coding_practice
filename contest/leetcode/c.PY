# # Definition for a binary tree node.
# from typing import List, Optional
#
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # 1. 找到root
        root_set = set()
        children_set = set()
        d = {}
        for node in descriptions:
            root_set.add(node[0])
            children_set.add(node[1])
            d.setdefault(node[0],[-1] * 2)
            if node[2] == 1:
                d[node[0]][0] = node[1]
            else:
                d[node[0]][1] = node[1]

        root = root_set - children_set
        root = root.pop()

        def build_tree(root):
            if root.val not in d:
                return root
            r_l = d[root][0]
            r_r = d[root][1]
            if r_l:
                root.left = build_tree(TreeNode(r_l))
            if r_r:
                root.right = build_tree(TreeNode(r_r))
            return root

        # 2. build
        return build_tree(TreeNode(root))


Solution().createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
