# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root == p or root == q:
            return root
        
        def LCA(child):
            if child is None:
                return None
            if child == p or child == q:
                return child
            
            left = LCA(child.left)
            right = LCA(child.right)

            if left and right:
                return child
            if left and right is None:
                return left
            if left is None and right:
                return right
            if left is None and right is None:
                return None


            

        return LCA(root)
            