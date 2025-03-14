# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def calc(n):
            if not n:
                v = TreeNode(val)
                return v

            if val < n.val:
                if not n.left:
                    n.left = TreeNode(val)
                else:
                    return calc(n.left)
               
            if  val > n.val:
                if not n.right:
                    n.right = TreeNode(val)
                else:
                    return calc(n.right)

        if not root:
            root = TreeNode(val)
        calc(root)
        return root

