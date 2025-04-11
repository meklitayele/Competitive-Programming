class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        store = defaultdict(list)
        for a , b in edges:
            store[b].append(a)

        print(store)
        res = []
        parents = []
        def dfs(node,visited):
            nonlocal parents 
            for n in store[node]:
                if n not in visited and n not in parents:
                    parents.append(n)
                    visited.add(n)
                    dfs(n,visited)
            return sorted(parents)

        for i in range(n):
            if i in store.keys():
                ans = dfs(i,set())
                res.append(ans)
                parents = []
            else:
                res.append([])
        return res

            
