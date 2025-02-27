# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        value = []
        curr = head
        
        while curr:
            value.append(curr.val)
            curr = curr.next

        value2 = value[::-1]
        half = len(value) // 2
        sums = 0
        for i in range(half):
            sum2 = value[i] + value2[i]
            sums = max(sums,sum2)
        return sums





        