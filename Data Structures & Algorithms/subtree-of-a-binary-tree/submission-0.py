# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Helper function to check if two trees are identical
        def SameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            # Recursively check left and right subtrees
            return SameTree(p.left, q.left) and SameTree(p.right, q.right)

        # Helper function for preorder traversal of the main tree
        def preorder_traversal(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            
            # If current node matches subRoot's root, check if the entire subtree matches
            if node.val == subRoot.val and SameTree(node, subRoot):
                return True
            
            # Recursively traverse the left and right subtrees
            return preorder_traversal(node.left) or preorder_traversal(node.right)

        # Start preorder traversal from the root
        return preorder_traversal(root)
