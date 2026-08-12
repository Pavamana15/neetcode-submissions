# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        output = 0

        def dfs(node):
            nonlocal output
            if not node:
                return []

            if not node.right and not node.left:
                return [node.val]

            
            
            

            left_digit = dfs(node.left)
            right_digit = dfs(node.right)
            

            return [str(node.val) + str(num) for num in left_digit+right_digit]

        res = dfs(root)
        print("digits are:", res)
        for num in res:
            output += int(num)

        return output

            
        