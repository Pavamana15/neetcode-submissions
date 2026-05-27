# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        # Helper function to calculate the maximum depth of a tree
        def maxDepth(node: TreeNode) -> int:
            if not node:
                return True
            
            # Recursively find the depth of the left and right subtrees
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)

            # If left or right subtree is unbalanced, return -1 immediately
            if left_depth == -1 or right_depth == -1:
                return -1
            
            # If the current node's subtrees differ in depth by more than 1, it's unbalanced
            if abs(left_depth - right_depth) > 1:
                return -1
            
            
                
            
            # Return the maximum depth from this node
            return max(left_depth, right_depth) + 1

        # Start DFS from the root to calculate depth and diameter
        maxDepth(root)
        
        return maxDepth(root) != -1
        