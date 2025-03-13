# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(n):
            if not n:
                return
            traverse(n.left)
            ans.append(n.val)
            traverse(n.right)
        
        traverse(root)
        return ans

            