# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sums = 0
        def bfs(root,sums):
            deq = deque([root])
            while deq:
                node = deq.popleft()
                if node.right:
                    deq.append(node.right)
                if node.left:
                    if not node.left.left and not node.left.right:
                        sums += node.left.val
                    deq.append(node.left)
            return sums
        return bfs(root,0)




            

            
        