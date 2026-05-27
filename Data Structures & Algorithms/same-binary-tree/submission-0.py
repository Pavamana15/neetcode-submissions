# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        # If one node is None and the other is not, trees are not the same
        if not p or not q:
            return False
        
        # If the values of the current nodes do not match, trees are not the same
        if p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        
        # Trees are the same if both left and right subtrees are the same
        return left_same and right_same