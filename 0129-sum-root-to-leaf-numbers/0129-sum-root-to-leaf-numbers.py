# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        def calc(node,num):  
            if not node:
                return 0
            curr = node.val
            num = num * 10 + curr
            
            if not node.right and not node.left:
                return num

            return calc(node.right,num) + calc(node.left,num)

        return calc(root,0)

        