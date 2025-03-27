class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def valid(nums,que,k):
            n = len(nums)
            diff = [0] * (n+1)
            for i , j , val in queries[:k]:
                diff[i] -= val
                if j + 1 < n + 1:
                    diff[j+1] += val
           
            
            for i in range(1,len(diff)):
                diff[i] += diff[i-1]
            for i in range(n):
                if nums[i] + diff[i] > 0:
                    return False
            
            return True
        
        left , right = 0 , len(queries)
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if valid(nums,queries,mid):
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1
        return ans


            
        