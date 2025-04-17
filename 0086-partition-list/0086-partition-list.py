# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], z: int) -> Optional[ListNode]:
        store1 = ListNode(0)
        store2 = ListNode(0)

        x , y = store1 , store2
        curr = head

        while curr:
            if curr.val < z:
                x.next = curr
                x = x.next
            else:
                y.next = curr
                y = y.next
            curr = curr.next
        
       
        y.next = None
        x.next = store2.next

        return store1.next


        
            




