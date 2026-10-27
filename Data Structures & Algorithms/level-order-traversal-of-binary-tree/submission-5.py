# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rez = []

        def dfs(node, deep):
            if node == None:
                return
            if len(rez)==deep:
                rez.append([])
            rez[deep].append(node.val)
            dfs(node.left, deep+1)
            dfs(node.right, deep+1)
        
        dfs(root, 0)
        return rez

        