class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        store = defaultdict(list)
        for index , num in enumerate(manager):
            store[num].append(index)
        

        def dfs(node,visited):
            maxTime = 0
            for ne in store[node]:
                if ne not in visited:
                    visited.add(ne)
                    maxTime = max(maxTime,dfs(ne,visited))
            return maxTime + informTime[node]
        # visited = set()
        # time = 0
        # for i in range(n):
        #     if i not in visited:
        #         visited.add(i)
        #         time += informTime[i]
        #         dfs(i,visited,time)
        visited = set()
        return dfs(headID,visited)

            