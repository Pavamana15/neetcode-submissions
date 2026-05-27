# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True  # An empty node is valid
            
            # Check if the current node's value is within the valid range
            if not (min_val < node.val < max_val):
                return False
            
            # Recursively check the left and right subtrees with updated ranges
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
        
        # Initial call starts with the full range of valid values (-∞ to +∞)
        return validate(root, float('-inf'), float('inf'))

       