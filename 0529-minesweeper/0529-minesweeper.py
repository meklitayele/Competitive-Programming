class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1,1),(-1,1),(1,-1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]
        n , m = len(board) , len(board[0])
        def inbound(x,y):
            return 0 <= x < n and 0 <= y < m

        deq = deque()
        deq.append((click[0],click[1]))
        visited = set()
        visited.add((click[0],click[1]))

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        while deq:
            x , y = deq.popleft()
            count = 0
            for dx , dy in directions:
                newx , newy = x + dx , y + dy
                if inbound(newx,newy) and board[newx][newy] == 'M':
                    count += 1
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for dx , dy in directions:
                    newx , newy = dx + x , dy + y
                    if inbound(newx,newy) and board[newx][newy] == 'E'and (newx,newy) not in visited:
                        deq.append((newx,newy))
                        visited.add((newx,newy))

        return board
                    

        
        

