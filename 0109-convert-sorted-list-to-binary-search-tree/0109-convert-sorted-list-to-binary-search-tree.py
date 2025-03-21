# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        curr = head
        store = []
        while curr:
            store.append(curr.val)
            curr = curr.next
        def construct(l,r):
            if l > r :
                return 
            mid = (l + r) //2
            left = construct(l,mid-1)
            right = construct(mid+1,r)

            return TreeNode(store[mid],left,right)
        return construct(0,len(store)-1)
             
        