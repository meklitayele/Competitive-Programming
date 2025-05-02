# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                arr.append(curr.val)
                curr = curr.next
        heapq.heapify(arr)
        count = 0
        n = len(arr)
        res = []
        while count < n:
            res.append(heappop(arr))
            count += 1
        
        head = ListNode(0)
        curr = head
        i = 0
        while i < len(res):
            curr.next = ListNode(res[i])
            curr = curr.next
            i += 1
        return head.next



