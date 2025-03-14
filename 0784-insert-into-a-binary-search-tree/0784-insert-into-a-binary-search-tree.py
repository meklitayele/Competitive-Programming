# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def calc(n,val):
            if not n:
                v = TreeNode(val)
                return v

            if val < n.val:
                n.left = calc(n.left,val)
                return n
    
            if  val > n.val:
                n.right = calc(n.right,val)
                return n
                
        if not root:
            root = TreeNode(val)
        calc(root,val)
        return root

