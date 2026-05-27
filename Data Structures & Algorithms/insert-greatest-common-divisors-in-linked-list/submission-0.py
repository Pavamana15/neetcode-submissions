# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        prev = head
        cur = head.next

        while cur:
            a = prev.val
            b = cur.val
            divisor = gcd(a,b)

            node = ListNode(divisor,cur)
            prev.next = node
            
            prev =  cur
            cur = cur.next

        return head
