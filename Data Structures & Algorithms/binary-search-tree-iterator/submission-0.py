# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.res.append(node.val)
            inorder(node.right)

        inorder(root)
        self.i = -1
        

    def next(self) -> int:
        self.i += 1
        return self.res[self.i]
        

    def hasNext(self) -> bool:
        if self.i + 1 >= len(self.res):
            return False
        else:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()