# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        def deep(root, m):
            if root==None:
                return 0
            m = max(root.val, m)
            r = deep(root.right, m)
            l = deep(root.left,m)
            if m == root.val:
                return 1 + r + l
            else:
                return r+l
        return deep(root, -200)
