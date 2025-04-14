# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        array = deque([root])
        res = []
        while array:
            curr = []
            count = len(array)
            for n in range(count):
                num = array.popleft()
                curr.append(num.val)
                if num.left:
                    array.append(num.left)
                if num.right:
                    array.append(num.right)
            res.append(curr)
        return res
                


