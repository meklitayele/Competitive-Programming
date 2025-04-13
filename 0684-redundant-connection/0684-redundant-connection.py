class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node,parent,visited):
            if node == parent:
                return True

            visited.add(node)
            for n in store[node]:
                if n not in visited:
                    if dfs(n,parent,visited):
                        return True
            return False
        store = defaultdict(list)
        for a ,b in edges:
            visited = set()
            if dfs(a,b,visited):
                return [a,b]
            store[a].append(b)
            store[b].append(a)
        return []
            