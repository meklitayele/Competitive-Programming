class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        start = 0
        size = len(arr)
        store = []
        for n in arr:
            start ^= n
            store.append(start)
        
        answer = []
        for x , y in queries:
            if x - 1 >= 0:
                ans = store[y] ^ store[x-1]
            else:
                ans = store[y] 
            answer.append(ans)
        
        return answer

        

