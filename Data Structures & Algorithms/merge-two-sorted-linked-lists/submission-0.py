# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 , head2 = list1, list2
        dummy = ListNode()
        current = dummy

        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            pointer1, pointer2 = head1, head2
            while pointer1 and pointer2:
                if pointer1.val <= pointer2.val:
                    current.next = pointer1
                    pointer1 = pointer1.next
                else:
                    current.next = pointer2
                    pointer2 = pointer2.next
                current = current.next
            if pointer1:
                current.next = pointer1
            elif pointer2:
                current.next = pointer2

        # Return the merged list starting from the first node
        return dummy.next
        
        
