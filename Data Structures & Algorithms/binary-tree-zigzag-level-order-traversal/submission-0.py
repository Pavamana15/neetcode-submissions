# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def levelOrder(root):
            if root is None:
                return -1

            q = deque([root])
            output = []
            level = 0

            while q:
                level_size = len(q)
                level_value = []

                for _ in range(level_size):
                    node = q.popleft()

                    level_value.append(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)
                
                if level % 2 == 0:
                    output.append(level_value)
                else:
                    level_value.reverse()
                    output.append(level_value)

                level += 1


                

            return output

        return levelOrder(root)