# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        deq = deque([root])
        ans = []
        while deq:
            n = len(deq)
            count = 1
            for _ in range(n):
                node = deq.popleft()
                if count == 1:
                    ans.append(node.val)
                    count -= 1
                if node.right:
                    deq.append(node.right)
                if node.left:
                    deq.append(node.left)
        return ans



        