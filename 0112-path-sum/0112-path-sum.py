# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        @cache
        def calc(node,total):
            if not node:
                return False

            total += node.val
            if not node.right and not node.left:
                return total == targetSum

            return calc(node.left,total) or calc(node.right,total)

        ans = calc(root,0)
        return ans
         
            
            
            


        