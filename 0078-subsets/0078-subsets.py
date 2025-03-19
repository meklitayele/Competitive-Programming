class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(index,store): 
            ans.append(store[:])
            for j in range(index,n):
                store.append(nums[j])
                print(store)
                backtrack(j+1,store)
                store.pop()
        backtrack(0,[])
        return ans

        
            



        