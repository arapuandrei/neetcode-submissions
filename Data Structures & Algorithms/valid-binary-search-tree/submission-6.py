# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def check(self, root, mi=None, ma=None):
        if root != None:
            if mi != None:
                if root.val <= mi:
                    return False
            if ma != None:
                if root.val >= ma:
                    return False
            return self.check(root.left,mi,root.val) and self.check(root.right, root.val, ma)
        return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, mi= None, ma = None)