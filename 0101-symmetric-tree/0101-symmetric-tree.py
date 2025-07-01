# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def search(n,m):
            if not n and not m:
                return True
            if not n or not m:
                return False
            
            return n.val == m.val and search(n.left,m.right) and search(n.right,m.left)
        return search(root.left,root.right)
       