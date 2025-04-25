class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)


        def dfs(node):
            for room in rooms[node]:
                if room not in visited:
                    visited.add(room)
                    dfs(room)
        dfs(0)
        return len(visited) == len(rooms) 
        







            