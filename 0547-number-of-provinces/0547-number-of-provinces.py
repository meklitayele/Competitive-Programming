class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        store = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i,len(isConnected)):
                if isConnected[i][j] == 1:
                    store[i].append(j)
                    store[j].append(i)

       
        def dfs(node,visited):
            visited.add(node)
            for n in store[node]:
                if n not in visited:
                    dfs(n,visited)
            
        visited = set()
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                dfs(i,visited)
        return count
          

            