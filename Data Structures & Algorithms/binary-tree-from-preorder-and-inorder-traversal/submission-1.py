# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        

        if not preorder or not inorder:
            return None
            
        root_value = preorder[0]
        root = TreeNode(root_value)

        left_inorder = inorder[:inorder.index(root_value)]
        right_inorder = inorder[inorder.index(root_value)+1:]

        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]
        
            
        root.left=     self.buildTree(left_preorder,left_inorder)
        
        root.right =     self.buildTree(right_preorder, right_inorder)

        
        return root

        
      


