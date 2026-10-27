# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deep(self, root):
        if root == None:
            return 0
        return max(self.deep(root.right)+1, self.deep(root.left)+1)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.isBalanced(root.right) and self.isBalanced(root.left) and abs(self.deep(root.right)-self.deep(root.left))<=1