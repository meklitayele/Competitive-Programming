# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        curr = head 
        while curr:
            values.append(curr.val)
            curr = curr.next

        if len(values) < k:
            return head

        #reverse in groups of k
        n = len(values)
        for i in range(0,n,k):
            if i + k <= n:
                values[i:i+k] = values[i:i+k][::-1]
        print(values)
        dummyNode = ListNode(0)
        current = dummyNode
        for val in values:
            current.next=ListNode(val)
            current= current.next

        return dummyNode.next



        # print(val3)

            

