# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    


            

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        mat = []
        def rdf(root, deep):
            if root is not None:
                if len(mat)==deep:
                    mat.append([])
                mat[deep].append(root.val)
                rdf(root.right, deep+1)
                rdf(root.left, deep+1)
        rdf(root,0)
        return [x[0] for x in mat]