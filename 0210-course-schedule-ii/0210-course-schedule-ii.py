class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        store = defaultdict(list)
        for a , b in prerequisites:
            store[b].append(a)

        color = ['white'] * numCourses
        res = []
        flag = False
        def dfs(node):
            nonlocal flag
            if color[node] == 'Grey':
                flag = True
                return 
            if color[node] == 'Black':
                return
            color[node] = 'Grey'
            for n in store[node]:
                dfs(n)
                if flag:
                    return
            color[node] = 'Black'
            res.append(node)
            


        for n in range(numCourses):
            if color[n] == 'white':
                dfs(n)
                if flag:
                    return []
    

        return res[::-1]


           
       

            
