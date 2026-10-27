# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        head1, prev1 , head2 , prev2 = l1,None, l2, None
        Output = ListNode(0)
        res = Output

        while head1:
            temp = head1.next
            
            head1.next = prev1
            prev1 = head1
            head1 = temp
            

        print(f"THe first linked list 1 is : {prev1}")

        while head2:
            temp = head2.next
            
            head2.next = prev2
            prev2 = head2
            head2 = temp
        
        print(f"THe first linked list 1 is : {prev2}")


        while prev1 or prev2 or carry:
            val1 = prev1.val if prev1 else 0
            val2 = prev2.val if prev2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            res.next = ListNode(total % 10)
            res = res.next

            if prev1:
                prev1 = prev1.next
            if prev2:
                prev2 = prev2.next

        
        prev = None 
        head = Output.next

        while head:
            temp = head.next
            
            head.next = prev
            prev = head
            head = temp
        
        return prev