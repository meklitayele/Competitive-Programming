# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        deq = deque()
        deq.append(root)
        final = []
        while deq:
            res = []
            count = len(deq)
            for _ in range(count):
                curr = deq.popleft()
                res.append(curr.val)
                if curr.left:
                    deq.append(curr.left)
                if curr.right:
                    deq.append(curr.right)
            final.append(res)
        return final
    
            


                


