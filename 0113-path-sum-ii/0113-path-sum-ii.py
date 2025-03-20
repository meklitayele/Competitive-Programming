# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return []
        
        def calc(node,store,curr):
            if not node:
                return
            curr += node.val
            store.append(node.val)

            if not node.right and not node.left and curr == targetSum:
                ans.append(store[:])

            calc(node.right,store,curr)
            calc(node.left,store,curr)

            store.pop()
        
        calc(root,[],0)
        return ans
            




        


        
            



        