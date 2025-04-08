class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        def build():
            for i, [a , b] in enumerate(equations):
                graph[a].append((b,values[i]))
                graph[b].append((a,1/values[i]))
        build()
        # print(dict(graph))
        
        def dfs(start,end,visited,pro):
            if start == end and graph[start] and graph[end] :
                return pro
            
            for d , v in graph[start]:
                # visited = visited.copy()
                if d not in visited:
                    visited.add(d)
                    ans =  dfs(d,end,visited,pro*v)
                    if ans != -1 :
                        return ans
                   
            return -1

            
        ans = []
        for a , b in queries:
            ans.append(dfs(a,b,set([a]),1))
        return ans







        