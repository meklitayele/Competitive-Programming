# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(n):
            if not n :
                return 
            ans.append(n.val)
            traverse(n.left)
            traverse(n.right)
            
        ans = []
        traverse(root)
        return ans
            
        



        






        