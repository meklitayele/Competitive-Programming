class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        n , m = len(board) , len(board[0])
        def inbound(x,y):
            return 0 <= x < n and 0 <= y < m

        def dfs(x,y):
            for dx , dy in directions:
                newx , newy = dx + x , dy + y
                if inbound(newx,newy) and board[newx][newy] == 'X':
                    board[newx][newy] = '.'
                    dfs(newx,newy)

        count = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    count += 1
                    dfs(i,j)
        return count
            