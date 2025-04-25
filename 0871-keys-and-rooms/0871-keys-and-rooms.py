class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        deq = deque()
        deq.append(0)

        while deq:
            node = deq.popleft()
            visited.add(node)
            for room in rooms[node]:
                if room not in visited:
                    deq.append(room)
        return len(visited) == len(rooms)
            



        







            