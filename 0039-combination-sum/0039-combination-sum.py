class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def backtrack(index,store):
            if sum(store) == target:
                ans.append(store[:])   
                return 
            for j in range(index ,n):
                if sum(store) < target:
                    store.append(candidates[j])
                    backtrack(j,store)
                    store.pop()
        backtrack(0,[])
        return ans

                
                

            # for num in candidates:
            #     total += num
            #     if total == target:
            #         print(store)
            #         ans.append(store[:])  
            #         return
            #     if total > target:
            #         continue
                
            #     backtrack(store,total)
            #     store.pop()

        # for num in candidates:
        #     if num == target:
        #         ans.append(num)
        #     else:
        #         backtrack([],0)
        return ans






        