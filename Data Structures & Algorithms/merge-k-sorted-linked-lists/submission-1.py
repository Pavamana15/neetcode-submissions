# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists( list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
class Solution: 
    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        Output = ListNode()
        i=0

        if  not lists:
            Output = None
            return Output
        else:
            i = 0
            while  len(lists) > 1:
                if i == 0:
                    LL1 = lists[i]
                    LL2 = lists[i+1]
                    Output = mergeTwoLists(LL1,LL2)
                    lists[0:2] = [Output]
                    i +=1
                else:
                    Output = mergeTwoLists(Output,lists[1])
                    lists[0:2] = [Output]
                    
            
            return Output

            
                


            