class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @cache
        def get(row,col):
            if col == 0 or row == col:
                return 1
            return get(row-1,col-1) + get(row-1,col)
        ans = [get(rowIndex,col) for col in range(rowIndex+1)]
        return ans
       

    
        
        
        