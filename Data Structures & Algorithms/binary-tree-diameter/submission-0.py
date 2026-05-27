# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            

        self.diameter = 0  # Initialize the diameter
        
        # Helper function to calculate the maximum depth of a tree
        def maxDepth(node: TreeNode) -> int:
            if not node:
                return 0
            
            # Recursively find the depth of the left and right subtrees
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)
            
            # Update the diameter if the current path is larger than the current max diameter
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the maximum depth from this node
            return max(left_depth, right_depth) + 1

        # Start DFS from the root to calculate depth and diameter
        maxDepth(root)
        
        return self.diameter