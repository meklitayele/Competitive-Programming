# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # try to slice it too
        def construct(l,r):
            if l>r:
                return None

            mid =  ( l + r) // 2
            left = construct(l,mid-1)
            right = construct(mid+1,r)

            return TreeNode(nums[mid],left,right)
        return construct(0,len(nums)-1)


        


            
        
            

        