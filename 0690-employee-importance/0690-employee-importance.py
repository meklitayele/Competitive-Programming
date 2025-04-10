"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        impEmployee= defaultdict(int)
        subEmployee = defaultdict(list)
        visited = set()
        for emp in employees:
            impEmployee[emp.id] = emp.importance
            for sub in emp.subordinates:
                subEmployee[emp.id].append(sub)
        
        total = 0
        def dfs(node):
            nonlocal total
            total += impEmployee[node]
            for sub in subEmployee[node]:
                if sub not in visited:
                    dfs(sub)
        dfs(id)
        return total



            


        # dfs(id)
            
      

        