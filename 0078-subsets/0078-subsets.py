class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = pow(2,len(nums))
        res = []
        
        # 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7
        for num in range(n): 
            sub = []
            for i in range(num): 
                if num & (1 << i): 
                    sub.append(nums[i])
            res.append(sub)

        return res


        