class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        n = len(arr)
        start = 0
        for i in range(n):
            start ^= arr[i]
            prefix.append(start)
        
        print(prefix)
        res = []
        
        for s , e in queries:
            s -= 1
            res.append(prefix[e] if s < 0 else prefix[e] ^ prefix[s])
           
        return res
