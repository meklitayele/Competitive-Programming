class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        for row in matrix:
            ans = bisect_left(row,target)
            if ans < n and row[ans] == target:
                return True
        return False
        
            