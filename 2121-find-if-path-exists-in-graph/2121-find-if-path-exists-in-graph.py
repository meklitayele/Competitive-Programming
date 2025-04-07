class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(node,visited):
            if node == destination:
                return True
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    found = dfs(n,visited)
                    if found :
                        return True
            return False

        graph = defaultdict(list)
        visited = set()
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        return dfs(source,visited)

            

