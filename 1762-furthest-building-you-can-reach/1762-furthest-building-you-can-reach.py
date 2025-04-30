class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []
        for i in range(1,len(heights)):
            if heights[i] - heights[i-1] > 0:
                heapq.heappush(arr,(heights[i] - heights[i-1]))
            if len(arr) > ladders:
                val = heappop(arr)
                bricks -= val
                if bricks < 0 :
                    return i- 1
                
        return len(heights) - 1

            
                

           