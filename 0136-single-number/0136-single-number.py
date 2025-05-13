class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        
        for key , val in store.items():
            if val == 1:
                return key
