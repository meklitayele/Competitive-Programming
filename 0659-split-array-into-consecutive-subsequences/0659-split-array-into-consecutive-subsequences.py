class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        #keep track of the ending numbers
        #if no number ends with num-1 the start a new one
        #instead of checking the gap check for num - 1
        endings = defaultdict(list)
        for num in nums:
            #the prior number exists
            if endings[num-1]:
                smallest = heapq.heappop(endings[num-1]) #the smallest subsequence
                heapq.heappush(endings[num],smallest+1)
            else:
                heapq.heappush(endings[num],1)
        
        for lst in endings.values():
            if lst and lst[0] < 3:
                return False
        return True
         




            