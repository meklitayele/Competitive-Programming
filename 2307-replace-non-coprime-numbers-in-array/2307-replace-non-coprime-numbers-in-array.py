class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if len(nums) == 1 or not nums:
            return nums

        store = []
        for num in nums:
            store.append(num)
            while len(store) > 1 and math.gcd(store[-1],store[-2]) > 1:
                a = store.pop()
                b = store.pop()
                store.append(math.lcm(a,b))
            
        
        # print(store)
        return store



       