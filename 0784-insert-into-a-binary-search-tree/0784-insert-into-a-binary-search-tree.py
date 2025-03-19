# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        
        curr = TreeNode(val)
        def calc(node,key):
            if not node:
                return curr
            if key < node.val:
                node.left = calc(node.left,key)
            elif key > node.val:
                node.right = calc(node.right,key)
            return node

        return calc(root,val)






       

