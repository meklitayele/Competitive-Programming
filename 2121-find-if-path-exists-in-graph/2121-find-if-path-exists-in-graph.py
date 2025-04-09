class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #build the neighbours
        store = defaultdict(list)
        for i , j in edges:
            store[i].append(j)
            store[j].append(i)

        
        def dfs(node,desitination,visited):
            if node == destination:
                return True
            for neighbour in store[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    if dfs(neighbour,destination,visited) == True:
                        return True
            return False

        visited = set()
        return dfs(source,destination,visited)
            
        
     