class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        store = defaultdict(list)
        color = ['white'] * numCourses
        for a , b in prerequisites:
            store[b].append(a)
        
        flag = False
        res  = []
        def bfs(node):
            nonlocal flag
            if color[node] == 'grey':
                flag = True
                return 
            if color[node] == 'black':
                return 
            color[node] = 'grey'

            for n in store[node]:
                bfs(n)
                if flag:
                    return 
            color[node] = 'black'
            res.append(node)

        
        for n in range(numCourses):
            if color[n] == 'white':
                bfs(n)
                if flag:
                    return []
        return res[::-1]
