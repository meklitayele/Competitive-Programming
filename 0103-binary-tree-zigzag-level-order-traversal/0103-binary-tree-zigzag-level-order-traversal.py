# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        flag = True
        deq = deque()
        deq.append(root)
        final = []

        while deq:
            res = []
            count = len(deq)
            for _ in range(count):
                v = deq.popleft()
                res.append(v.val)
                if v.left:
                    deq.append(v.left)
                if v.right:
                    deq.append(v.right)
            if not flag:
                final.append(res[::-1])
                flag = True
            else:
                final.append(res)
                flag = False
                    
            
        return final

