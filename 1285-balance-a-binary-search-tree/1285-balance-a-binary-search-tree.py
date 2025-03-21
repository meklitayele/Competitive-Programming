# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(node):
            if not node :
                return 
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        def divide(l,r):
            if l > r:
                return 
            mid = (l + r) // 2
            left = divide(l,mid-1)
            right = divide(mid+1,r)

            return TreeNode(arr[mid],left,right)
        inorder(root)
        return divide(0,len(arr)-1)



        