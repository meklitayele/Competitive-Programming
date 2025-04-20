# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt = 0
        def search(root):
            nonlocal cnt

            if not root:
                return (0,0)
            ls , lc = search(root.left)
            rs , rc = search(root.right)

            sums = ls + rs + root.val
            count = lc + rc + 1

            if sums//count == root.val:
                cnt += 1
            
            return (sums,count)

        search(root)
        return cnt
        