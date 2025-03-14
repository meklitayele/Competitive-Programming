# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums = 0
        @cache 
        def calc(n,sums):
            if not n:
                return False
            sums += n.val
            if not n.left and not n.right:
                return sums == targetSum
            
            return calc(n.left,sums) or calc(n.right,sums)
                
        
        answer = calc(root,sums)
        return answer
            
            
            


        