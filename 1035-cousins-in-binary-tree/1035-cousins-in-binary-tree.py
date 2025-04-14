# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        array = deque([root])
        res = []
        parent = defaultdict(int)
        while array:
            curr = []
            count = len(array)
            for _ in range(count):
                num = array.popleft()
                curr.append(num.val)
                if num.left:
                    parent[num.left.val]=(num.val)
                    array.append(num.left)
                if num.right:
                    parent[num.right.val]=(num.val)
                    array.append(num.right)
            res.append(curr)
        print(parent)
        cousin = 2
        for v in res:
            for i in v:
                if i == x:
                    cousin -= 1
                if i == y:
                    cousin -= 1
                if cousin == 0 :
                    if parent[x] != parent[y]:
                        return True
            cousin = 2
        


        # if [x,y] in res or [y,x] in res:   
        #     if parent[x] != parent[y]:
        #         return True
        #     else:
        #         return False
        return False   