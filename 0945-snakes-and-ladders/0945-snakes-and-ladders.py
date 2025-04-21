class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def getCoord(curr):
            row , col = (curr - 1)//n , (curr-1) % n
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row , col
        
        deq = deque()
        deq.append(1)
        visited = set()
        visited.add(1)
        moves = 0

        while deq:
            for _ in range(len(deq)):
                curr = deq.popleft()
                if curr == n*n:
                    return moves
                for nxt in range(curr + 1, min(curr + 7, n*n+1)):
                    r , c = getCoord(nxt)
                    if board[r][c] != -1:
                        nxt = board[r][c]
                    if nxt not in visited:
                        visited.add(nxt)
                        deq.append(nxt)
            moves += 1
        return -1


            
