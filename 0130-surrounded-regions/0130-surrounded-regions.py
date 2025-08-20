class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        n , m = len(board) , len(board[0])

        def inbound(x,y):
            return 0 <= x < n and 0 <= y< m

        def dfs(x,y):
            if board[x][y] != 'O':
                return 
            board[x][y] = 's'
            deq = deque([(x,y)])
            while deq:
                x , y = deq.popleft()
                for dx , dy in directions:
                    newx , newy = x + dx , y + dy
                    if inbound(newx,newy) and board[newx][newy] == 'O':
                        board[newx][newy] = 's'
                        deq.append((newx,newy))
                        dfs(newx,newy)
        
        for r in range(len(board)):
            dfs(r,0)
            dfs(r,m-1)
        for c in range(len(board[0])):
            dfs(0,c)
            dfs(n-1,c)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 's':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return board

        