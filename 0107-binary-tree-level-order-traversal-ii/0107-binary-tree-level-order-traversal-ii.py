# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        deq = deque([root])
        while deq:
            curr = []
            count = len(deq)
            for _ in range(count):
                node = deq.popleft()
                curr.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            ans.append(curr)
        return ans[::-1]