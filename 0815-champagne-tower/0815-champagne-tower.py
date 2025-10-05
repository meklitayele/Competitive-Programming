class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * size for size in range(1,101)]
        dp[0][0] = float(poured) #the first glass takes everything in 
        
        # print(dp)
        for i in range(1,query_row+1):
            for j in range(i+1):
                left_pour , right_pour = 0.0 , 0.0
                if j - 1 >= 0:
                    left_pour = max(0.0,dp[i-1][j-1]-1.0) / 2
                if j < len(dp[i-1]) :
                    right_pour = max(0.0,dp[i-1][j]-1.0) / 2

                dp[i][j] = left_pour + right_pour
                
        return min(1.0,dp[query_row][query_glass])
