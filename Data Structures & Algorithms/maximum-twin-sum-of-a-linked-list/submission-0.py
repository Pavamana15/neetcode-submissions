# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        cur = head

        while cur:
            values.append(cur.val)
            cur = cur.next

        output = 0
        n = len(values)

        for i in range(n // 2):
            output = max(output, values[i] + values[n - 1 - i])

        return output