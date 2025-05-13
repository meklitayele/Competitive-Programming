class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        m = len(baseStr)
        parent = {}
        for ch in range(26):
            parent[chr(ord('a')+ch)] = chr(ord('a')+ch)
        # print(parent)


        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            r1 , r2 = find(x) , find(y)
            if r1 != r2:
                if ord(r1) < ord(r2):
                    parent[r2] = r1
                else:
                    parent[r1] = r2
        
        n = len(s1)
        for i in range(n):
            union(s1[i] , s2[i])
        
        word = []
        for i in range(m):
            word.append(find(baseStr[i]))
        return (''.join(word))


    

