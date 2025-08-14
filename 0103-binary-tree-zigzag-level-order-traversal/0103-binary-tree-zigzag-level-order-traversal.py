# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = False
        deq = deque([root])
        ans = []
        if not root:
            return ans
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
            if not flag:
                ans.append(curr)
                flag = True
            else:
                ans.append(curr[::-1])
                flag = False
        return ans