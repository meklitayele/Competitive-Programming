class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        store = defaultdict(list)
        for i , j in edges:
            store[i].append(j)
        
        visited = set()
        def dfs(node,visited):
            for n in store[node]:
                if n not in visited:
                    visited.add(n)
                    dfs(n,visited)

       

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i,visited)
                if len(visited) == n:
                    return i
            visited = set()   

       
        return -1

                

            
                    
