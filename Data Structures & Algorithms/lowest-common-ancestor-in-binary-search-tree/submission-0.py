# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def exist(self,root, n):
        if root is not None:
            if root==n:
                return True
            else:
                return self.exist(root.left,n) or self.exist(root.right, n)
        return False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is not None:
            if (self.exist(root.left, p) and self.exist(root.left,q)):
                print("stanga")
                return self.lowestCommonAncestor(root.left, p,q)
            if (self.exist(root.left, p) and self.exist(root.right,q)):
                print("aici")
                return root
            if (self.exist(root.right, p) and self.exist(root.right,q)):
                print("dreapta")
                return self.lowestCommonAncestor(root.right, p,q)
        return root