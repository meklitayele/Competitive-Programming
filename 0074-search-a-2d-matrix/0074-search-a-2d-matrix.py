class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i , j = len(matrix) , len(matrix[0])
        left , right = 0 , (i*j)-1

        while left <= right:
            mid = (left + right)//2
            row,col = mid//j, mid%j
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
