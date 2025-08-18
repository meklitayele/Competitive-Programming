class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n , m = len(matrix) , len(matrix[0])
        store = []
        for i in range(n):
            for j in range(m):
                store.append(matrix[i][j])
        heapify(store)
        while k > 1:
            heapq.heappop(store)
            k -= 1
        val = heapq.heappop(store)
        return (val)

        