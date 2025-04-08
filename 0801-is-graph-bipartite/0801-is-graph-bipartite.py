class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n 

        def dfs(node,color):
            colors[node] = color
            for n in graph[node]:
                if colors[n] == -1 and not dfs(n,color ^ 1):
                    return False
                elif colors[n] == colors[node]:
                    return False
            return True

        for i in range(n):
            if colors[i] == -1:
                if not dfs(i,0):
                    return False
        return True



        