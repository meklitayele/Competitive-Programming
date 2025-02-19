# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0 , None)
        dummy.next = head
        curr = head
        prev = dummy 

        while curr:
            if curr.val == val:
                temp = curr
                prev.next = curr.next
                curr = curr.next
                temp.next = None
            else:
                prev = prev.next
                curr = curr.next
     
        return dummy.next







        