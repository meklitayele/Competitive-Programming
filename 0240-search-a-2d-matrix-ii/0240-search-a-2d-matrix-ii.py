class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = len(matrix[0])
        for row in matrix:
            ans = bisect_left(row,target)
            if ans < l and row[ans]  == target:
                return True
        return False
        
            