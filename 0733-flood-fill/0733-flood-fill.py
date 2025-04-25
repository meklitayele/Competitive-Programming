class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n , m = len(image) , len(image[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(x,y):
            return 0<=x<n and 0<=y<m


        deq = deque()
        deq.append((sr,sc))
        org = image[sr][sc]
        if org == color:
            return image
            
        while deq:
            x , y = deq.popleft()
            image[x][y] = color
            for dx , dy in directions:
                newx , newy = x + dx , y + dy
                if inbound(newx,newy) and image[newx][newy] == org:
                    image[newx][newy] = color
                    deq.append((newx,newy))
        return image

      