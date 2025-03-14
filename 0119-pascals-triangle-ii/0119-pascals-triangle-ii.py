class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @cache
        def calc(row,col):
            if row == col:
                return 1
            if col == 0:
                return 1
            else:
                return calc(row-1,col-1) + calc(row-1,col)
        ans = [calc(rowIndex,col) for col in range(rowIndex+1)]
        return ans

            
           

        

    
        
        
        