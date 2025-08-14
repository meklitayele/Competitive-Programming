# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #more appropriate to use BFS
        if not root:
            return 0
        deq = deque([(root,1)])
        while deq:
            node , depth = deq.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                deq.append([node.left,depth+1])
            if node.right:
                deq.append([node.right,depth+1])
    
        