class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [-1] * (n + 1)
        store = defaultdict(list)
        for a , b in dislikes:
            store[a].append(b)
            store[b].append(a)


        def dfs(node,color):
            colors[node] = color
            for ne in store[node]:
                if colors[ne] == -1 and not dfs(ne,color ^ 1):
                    return False
                elif colors[ne] == colors[node]:
                    return False
            return True

        for val in range(1,n+1):
            if colors[val] == -1:
                if not dfs(val,0):
                    return False
        return True
        


