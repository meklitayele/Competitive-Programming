class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        store = defaultdict(list)
        for a , b in edges:
            store[a].append(b)
            store[b].append(a)

        visited = set()
        count = 0
        
        def dfs(node,component):
            component.add(node)
            visited.add(node)
            for n in store[node]:
                if n not in visited:
                    dfs(n,component)

            
        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i,component)  
                if all(len(store[node]) == len(component)-1 for node in component):
                    count += 1


        return count


