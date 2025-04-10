class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        store = defaultdict(list)
        for serve , boss in enumerate(manager):
            store[boss].append(serve)
        
        def dfs(node,visited):
            maxTime = 0
            for under in store[node]:
                if under not in visited:
                    visited.add(under)
                    maxTime = max(maxTime , dfs(under,visited))
            return maxTime + informTime[node]

        visited = set()
        return dfs(headID,visited)

                
