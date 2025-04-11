class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(r,c):
            return 0<=r<len(board) and 0<=c<len(board[0])
       
        def dfs(row,col):
            if inbound(row,col) and board[row][col] == 'O':
                board[row][col] = 's'
                for dx , dy in directions:
                    newX , newY = row + dx , col + dy
                    dfs(newX,newY)
        for r in range(len(board)):
            dfs(r,0)
            dfs(r,len(board[0])-1)

        for c in range(len(board[0])):
            dfs(0,c)
            dfs(len(board)-1,c)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 's':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
       
                    



        