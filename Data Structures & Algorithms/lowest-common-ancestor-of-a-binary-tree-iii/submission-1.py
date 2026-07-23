"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def LCA(child):
            if child is None:
                return None

            if child == p or child == q:
                return child

            left = LCA(child.left)
            right = LCA(child.right)

            if left and right:
                return child

            if left:
                return left

            if right:
                return right

            return None

        return LCA(root)
        