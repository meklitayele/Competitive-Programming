# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        store = deque([root])
        ans = []
        while store:
            rowMax = store[0].val
            for _ in range(len(store)):
                node = store.popleft()
                rowMax = max(rowMax , node.val)
                if node.right:
                    store.append(node.right)
                if node.left:
                    store.append(node.left)
            ans.append(rowMax)
        return ans