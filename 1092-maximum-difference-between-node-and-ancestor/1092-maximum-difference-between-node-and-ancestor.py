# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0
        def search(root,currMin,currMax):
            nonlocal diff
            if not root:
                return 

            currMin = min(root.val , currMin)
            currMax = max(root.val , currMax)
            diff = max(diff,currMax - currMin)

            search(root.left,currMin,currMax)
            search(root.right,currMin,currMax)
            
        search(root,root.val,root.val)
        return diff


            





