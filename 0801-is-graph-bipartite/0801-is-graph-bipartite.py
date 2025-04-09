class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        def dfs(node,color):
            if node in colors:
                return colors[node] == color #becuase i passed the opposite value

            colors[node] = color
            for neighbour in graph[node]:
                if not dfs(neighbour,1 -color ):
                    return False
            return True
        
        for i in range(len(graph)):
            if i not in colors:
                if not dfs(i,0):
                    return False
        return True
        
        
        