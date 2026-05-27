# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tail1 = l1
        tail2 = l2
        list1 = []
        list2 = []
        while tail1:
            list1.append(tail1.val)
            tail1 = tail1.next
        
        while tail2:
            list2.append(tail2.val)
            
            tail2 = tail2.next
        
        Added_Number  = int(''.join(map(str, reversed(list1)))) + int(''.join(map(str, reversed(list2))))
        print("Added Number:",Added_Number)
        reversed_list = [int(digit) for digit in str(Added_Number)] 
        print("Revered List:", reversed_list) 
        
        head = None
        for element in reversed_list:
            new_node = ListNode(val=element)  # Create a new node with the current element
            new_node.next = head  # Set the next pointer of the new node to the current head
            head = new_node  # Update the head to the new node
        
        return head
        

