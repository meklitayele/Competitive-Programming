class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set((entrance[0],entrance[1]))
        queue = deque()
        queue.append((entrance[0],entrance[1],0))
        
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(x,y):
            return 0 <= x < len(maze) and 0 <= y < len(maze[0])
        while queue:
            x , y , move = queue.popleft()
            # print(x, y)
            if (x == 0 or x == len(maze)-1 or y == 0 or y == len(maze[x])-1) and ([x, y]!=entrance):
                return move
            for dr, dc in dir:
                newX , newY = x + dr , y + dc
                if inbound(newX,newY) and maze[newX][newY] == '.':
                    visited.add((newX,newY))
                    queue.append((newX,newY,move+1))
        return -1
                


