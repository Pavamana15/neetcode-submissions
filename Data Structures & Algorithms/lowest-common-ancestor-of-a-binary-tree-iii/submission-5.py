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
        a = p
        b = q

        while a != b:
            if a:
                a = a.parent
            else:
                a = q

            if b:
                b = b.parent
            else:
                b = p

        return a
        
#         # def LCA(child):
#         #     if child is None:
#         #         return None

#         #     if child == p or child == q:
#         #         return child

#         #     left = LCA(child.left)
#         #     right = LCA(child.right)

#         #     if left and right:
#         #         return child

#         #     if left:
#         #         return left

#         #     if right:
#         #         return right

#         #     return None

#         # curr = p

#         # while curr.parent:
#         #     curr = curr.parent

#         # root = curr

#         # return LCA(root)


#         parents = set()

#         curr = p

#         while curr:
#             parents.add(curr)
#             curr = curr.parent
            
#         curr = q 
#         while curr:
#             if curr in parents:
#                 return curr
#             parents.add(curr)
#             curr = curr.parent

#         return curr


        




        
        