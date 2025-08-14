# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        deq = deque([root])
        if not root:
            return []
        
        while deq:
            n = len(deq)
            curr = []
            for _ in range(n):
                node = deq.popleft()
                curr.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            ans.append(curr)
        return ans
                

