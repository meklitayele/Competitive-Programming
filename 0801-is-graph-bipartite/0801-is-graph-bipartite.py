class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n 

        def dfs(node, color):
            colors[node] = color
            for neighbour in graph[node]:
                if colors[neighbour] == -1:
                    if not dfs(neighbour, color ^ 1):  
                        return False
                elif colors[neighbour] == colors[node]: 
                    return False
            return True  

        for i in range(n):
            if colors[i] == -1:  
                if not dfs(i, 0):  
                    return False

        return True  