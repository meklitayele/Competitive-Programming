class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        color = ['white' for _ in range(n)]
        store = defaultdict(list)

        for i , j in prerequisites:
            store[i].append(j)
        
        def dfs(node):
            if color[node] == 'grey':
                return False
            if color[node] == 'black':
                return True

            color[node] = 'grey'
            for n in store[node]:
                if not dfs(n):
                    return False
            color[node] = 'black'
            return True

        for i in range(n):
            if not dfs(i):
                return False
        return True
