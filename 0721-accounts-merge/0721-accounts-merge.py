class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = {i:i for i in range(n)}
        size = [1] * n

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            r1 = find(x)
            r2 = find(y) 
            if r1 != r2:
                if size[r1] > size[r2]:
                    size[r1] += size[r2]
                    parent[r2] = r1
                else:
                    size[r2] += size[r1]
                    parent[r1] = r2

        relation= {}
        for i , account in enumerate(accounts):
            for email in account[1:]:
                if email in relation:
                    union(i,relation[email])
                else:
                    relation[email] = i
        print(relation)

        emailrel = defaultdict(list)
        for key , val in relation.items():
            name = find(val)
            emailrel[name].append(key)
        print(emailrel)
        
        ans = []
        for key , val in emailrel.items():
            name = accounts[key][0]
            ans.append([name] + sorted(emailrel[key]))
        return ans

    
        

                



