class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        deq = deque()
        visited = set()
        visited.add((click[0],click[1]))
        deq.append((click[0],click[1]))
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        def inbound(r,c):
            return 0<=r<len(board) and 0<=c<len(board[0])

        while deq:
            r , c = deq.popleft()
            store = []
            count = 0
            for dx , dy in directions:
                newx , newy = r + dx , c + dy
                if inbound(newx,newy) :
                    if board[newx][newy] == 'M':
                        count += 1
                    elif board[newx][newy] == 'E':
                        store.append((newx,newy))
            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = 'B'
                for x , y in store :
                    if (x,y) not in visited:
                        deq.append((x,y))
                        visited.add((x,y))



        return board




