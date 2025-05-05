class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        parents = defaultdict(str)
        size = defaultdict(int)

        def find(x):
            if parents[x] == x:
                return x
            parents[x] = find(parents[x])
            return parents[x]
        
        def union(x,y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                if size[r1] > size[r2]:
                    size[r1] += size[r2]
                    parents[r2] = r1
                else:
                    size[r2] += size[r1]
                    parents[r1] = r2

        for w in equations:
            if w[0] == w[3] and w[1] == '!':
                return False
            if w[0] not in parents:
                parents[w[0]] = w[0]
                size[w[0]] = 1
            if w[3] not in parents:
                parents[w[3]] = w[3]
                size[w[0]] = 1
        
        #always do union first
        for word in equations:
            w1 , w2 = word[0] , word[3]
            e1 , e2 = word[1] , word[2]
            if e1 == '=':
                union(w1,w2) 
        print(parents)
       
        for word in equations:
            w1 , w2 = word[0] , word[3]
            e1 , e2 = word[1] , word[2]
            if e1 == '!':
                print(find(w1))
                print(find(w2))
                if find(w1) == find(w2):
                    return False
        print(parents)
            
    
        return True

                    


