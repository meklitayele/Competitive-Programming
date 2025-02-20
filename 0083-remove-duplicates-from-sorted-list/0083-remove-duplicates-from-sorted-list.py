# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(None,None)
        dummyNode.next = head
        curr = head
        prev = dummyNode

        while curr:
            if curr.val != prev.val:
                curr = curr.next
                prev = prev.next
            
            else:
                prev.next = curr.next
                curr = curr.next

        return dummyNode.next



        