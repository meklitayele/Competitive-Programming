class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0 , len(nums)-1
        mini = float('inf')
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > nums[right]: 
                mini = min(mini,nums[right])
                left = mid + 1
            else:
                mini = min(mini,nums[mid])
                right = mid - 1
        return mini
            