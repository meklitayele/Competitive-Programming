class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(r,c):
            return  0 <= r < len(board) and 0 <= c < len(board[0])
        
        #dfs accros all the edges 
        #assign diff variable to 0 at the edges
        def dfs(x,y):
            if board[x][y] != 'O':
                return 

            deq = deque()
            deq.append((x,y))
            board[x][y] = 's'
            while deq:
                x , y = deq.popleft()
                for dx , dy in directions:
                    newx , newy = dx + x , dy + y
                    if  inbound(newx,newy) and board[newx][newy] == 'O':
                        board[newx][newy] = 's'
                        deq.append((newx,newy))

        for r in range(len(board)):
            dfs(r,0)
            dfs(r,len(board[0])-1)

        for c in range(len(board[0])):
            dfs(0,c)
            dfs(len(board)-1,c)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 's':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        




                    
