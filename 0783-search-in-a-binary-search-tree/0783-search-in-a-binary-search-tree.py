# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def calc(n):
            if not n:
                return None
            # print(n.val)

            if val > n.val:
                return calc(n.right)
            if val < n.val:
                return calc(n.left)  
            if val == n.val:
                return n

        
        ans = calc(root)
        return ans

