class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        store = defaultdict(list)
        for i , j in edges:
            store[i].append(j)
        
        def dfs(node,visited):
            for ne in store[node]:
                if ne not in visited:
                    visited.add(ne)
                    dfs(ne,visited)
               


        visited = set()
        for i in range(n):
            visited.add(i)
            dfs(i,visited)
            if len(visited) == n:
                return i
            visited = set()

        return - 1

            