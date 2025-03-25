class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       
        left , right = 0 , len(nums)-1
        idx1 = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                idx1 = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1

        idx2 = -1
        left , right = 0 , len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                left = mid + 1
                idx2 = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return [idx1,idx2]

