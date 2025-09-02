class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for _ in range (numRows)]
        n = len(s)
        i = 0

        while i < n:
            for d in range(numRows):
                if i < n:
                    arr[d].append(s[i])
                    i += 1
            
            for u in range(numRows-2,0,-1):
                if i < n:
                    arr[u].append(s[i])
                    i += 1
        # print(arr)
        res = []
        for row in arr:
            res.extend(a for a in row)
        # print(res)
        return(''.join(res))
        


