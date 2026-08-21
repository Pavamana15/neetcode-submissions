# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # running_sum = 0
        
        # def inorder(node):
        #     nonlocal running_sum
        #     if not node:
        #         return

        #     inorder(node.right)

        #     a = node.val
        #     node.val +=  running_sum
        #     running_sum += a
            
        #     inorder(node.left)

        # inorder(root)

        # return root

        running_sum = 0
        stack = []
        node = root

        while stack or node:

            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()

            node.val += running_sum
            running_sum = node.val

            node = node.left
        
        return root