class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        store = defaultdict(list)
        count = 0
        for a , b in equations:
            store[a].append((b,values[count]))
            store[b].append((a,1/values[count]))
            count += 1

        def dfs(start,end,vis,pro):
            if start == end and store[start] and store[end]:
                return pro
            for v , p in store[start]:
                if v not in vis:
                    vis.add(v)
                    ans = dfs(v,end,vis,pro*p)
                    if ans != -1:
                        return ans
            return -1

        res = []
        for a , b in queries:
            res.append(dfs(a,b,set([a]),1))
        return res

            




        