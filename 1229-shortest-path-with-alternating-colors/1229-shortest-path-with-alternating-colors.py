class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for x , y in redEdges:
            red[x].append(y)
        for x , y in blueEdges:
            blue[x].append(y)

        res = [-1] * n
        visited = [[False,False] for _ in range(n)] #node,color
        #node , color , distance
        deq = deque()
        deq.append((0,0,0))
        deq.append((0,1,0))
        visited[0][0] = visited[0][1] = True

        while deq:
            node , color , dist = deq.popleft()
            if res[node] == -1:
                res[node] = dist
            else:
                res[node] = min(res[node],dist)

            if color == 0:
                for n in blue[node]:
                    if not  visited[n][1]:
                        visited[n][1] = True
                        deq.append((n,1,dist+1))
            else:
                for n in red[node]:
                    if not  visited[n][0]:
                        visited[n][0] = False
                        deq.append((n,0,dist+1))
        return res
    
        
        


        

        