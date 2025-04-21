class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        deq = deque()
        deq.append(1)
        visited = set()
        visited.add(1)
        move = 0
         

        def cord(curr):
            r , c = (curr - 1) // n , (curr - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r , c
        
        while deq:
            for _ in range(len(deq)):
                curr = deq.popleft()
                if curr == n**2:
                    return move

                for nxt in range(curr+1,min(curr+7,n*n+1)):
                    r , c = cord(nxt)
                    if board[r][c] != -1:
                        nxt = board[r][c]
                    if nxt not in visited:
                        visited.add(nxt)
                        deq.append(nxt)
            move += 1
        return -1



            