class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        n , m = len(matrix) , len(matrix[0])
        for i in range(n):
            for j in range(m):
                arr.append(matrix[i][j])
                
        heapq.heapify(arr)
        count = 1
        while count < k :
            heapq.heappop(arr)
            count += 1
        return arr[0]

