class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        store = defaultdict(int)
        n = len(stones)
        for i , val in enumerate(stones):
            store[val] = i
    

        def calc(jump,idx):
            if idx == n-1:
                return True           

            if (jump,idx)in dp:
                return dp[(jump,idx)]

            values = [jump , jump-1,jump+1]
            for v in values:
                if v > 0:
                    next_pos = stones[idx] + v
                    if next_pos in stones:
                        if calc(v,store[next_pos]):
                            dp[(jump,idx)] = True
                            return True
                    
            dp[(jump,idx)] = False
            return dp[(jump,idx)]
        return calc(0,0)


            

            