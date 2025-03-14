# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def go(n):
            if not n:
                return 
            ans.append(n.val)
            go(n.left)
            go(n.right)
        go(root)
        return ans
        
        



        






        