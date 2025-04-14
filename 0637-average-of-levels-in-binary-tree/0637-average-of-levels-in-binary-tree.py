# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        array = deque([root])
        res = []
        while array:
            count = len(array)
            sums = 0
            for _ in range(count):
                num = array.popleft()
                sums += num.val
                if num.left:
                    array.append(num.left)
                if num.right:
                    array.append(num.right)
            answer = sums / count
            res.append(answer)
        return res

        