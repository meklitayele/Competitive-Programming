class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        store[0] = 1
        ans = 0
        sums = 0

        for num in nums:
            sums += num
            ans += store[sums-k]
            store[sums] += 1
        
        return ans

       

         
        