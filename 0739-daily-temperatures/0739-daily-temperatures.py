class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #the gap to the next greater temp day
        n = len(temperatures)
        ans = [0] * n
        store = []

        for i in range(n):
            curr = temperatures[i]
            while store and curr > temperatures[store[-1]]:
                ans[store[-1]] = i - store[-1]
                store.pop()
            store.append(i)
           

        return (ans)





      

       