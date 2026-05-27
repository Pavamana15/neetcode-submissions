# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def addnode(node):
            if node is None:
                return TreeNode(val)         

            if val < node.val:
                node.left = addnode(node.left)   
            else:
                node.right = addnode(node.right) 

            return node                        


        
        return addnode(root)