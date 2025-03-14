class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def calc(arr):
            if len(arr) == 1:
                return arr[0]
            nextRow = [(arr[i] + arr[i+1]) % 10 for i in range(len(arr)-1)]
            return calc(nextRow)

        ans = calc(nums)
        return ans
        
        

    





        