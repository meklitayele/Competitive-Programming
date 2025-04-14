# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        array = deque()
        array.append(root)
        first = root.val

        while array:
            num = array.popleft()
            if  num.val != first:
                return False
            if num.left:
                array.append(num.left)
            if num.right:
                array.append(num.right)   
    
        return True
       
        