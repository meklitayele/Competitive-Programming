class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        index = []
        n = len(arr)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i < j <= k :
                        index.append((i,j,k))
        prefix = []
        ans = 0
        for n in arr:
            ans ^= n
            prefix.append(ans)
        
        result = []
        for i , j , k in index:
            if i-1 < 0 and prefix[j-1] == prefix[j-1] ^ prefix[k]:
                result.append((i,j,k))
            elif i-1 >= 0 and j-1 >= 0 and prefix[i-1] ^ prefix[j-1] == prefix[j-1] ^ prefix[k]:
                result.append((i,j,k))
        return (len(result))


