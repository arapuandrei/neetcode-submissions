# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkhere(self, root, subRoot):
        if root == None and subRoot== None:
            return True
        elif root != None and subRoot != None:
            here = root.val == subRoot.val and self.checkhere(root.left, subRoot.left) and self.checkhere(root.right, subRoot.right)
            return here
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot== None:
            return True
        elif root != None and subRoot != None:
            here = root.val == subRoot.val and self.checkhere(root.left, subRoot.left) and self.checkhere(root.right, subRoot.right)
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            print("sub",root.val, subRoot.val, here, left, right)
            return here or right or left
        return False