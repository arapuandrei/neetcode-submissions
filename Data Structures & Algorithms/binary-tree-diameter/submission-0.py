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
        return max(self.deep(root.right)+1 , self.deep(root.left)+1)

    def check(self, root):
        return self.deep(root.right)+self.deep(root.left)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.check(root), self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))