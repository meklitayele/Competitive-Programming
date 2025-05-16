class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        start = 0
        for val in arr:
            start ^= val
            prefix.append(start)
        
        res = []
        for l , r in queries:
            l -= 1
            if l < 0 :
                res.append(prefix[r])
            else:
                res.append(prefix[r] ^ prefix[l])
        return res

