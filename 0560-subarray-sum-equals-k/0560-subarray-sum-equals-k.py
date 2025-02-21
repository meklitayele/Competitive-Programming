class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        store[0] = 1
        sums = 0
        ans = 0
        for i in range(len(nums)):
            sums += nums[i]
            ans += store[sums-k]
            store[sums] += 1
        return ans


        
       



    
       

       

         
        