class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        deq = deque()
        deq.append((sr,sc,color))
        visited =[(sr,sc)]
        
        start = image[sr][sc]
        image[sr][sc] = color
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(r,c):
            return 0<=r<len(image) and 0<=c<len(image[0])

        while deq:
            r , c , color = deq.popleft()
            for dx , dy in directions:
                newx , newy = dx + r , dy + c
                if inbound(newx,newy) and image[newx][newy] == start and (newx,newy)not in visited:
                    visited.append((newx,newy))
                    image[newx][newy] = color
                    deq.append((newx,newy,color))
                    
        return image

