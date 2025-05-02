class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        n , m = len(matrix) , len(matrix[0])
        for i in range(n):
            for j in range(m):
                ans.append(matrix[i][j])
        heapq.heapify(ans)
        res = heapq.nsmallest(k,ans)
        return (res[-1])
        

