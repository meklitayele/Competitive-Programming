class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        store = []
        i = 1
        while i < len(heights):
            diff = heights[i] - heights[i-1] 
            if diff > 0:
                heapq.heappush(store,diff)
            if len(store) > ladders:
                minVal = heapq.heappop(store)
                bricks -= minVal
                if bricks < 0:
                    return i-1
            i += 1
        return len(heights) - 1


            
                

           