# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
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
                
            final.append(res)

        return final[::-1]
