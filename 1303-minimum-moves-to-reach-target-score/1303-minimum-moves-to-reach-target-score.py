class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles and target:
            if target % 2 == 0 :
                maxDoubles -= 1
                target //=  2
            else:
                target -= 1
            count += 1

        return target + count - 1 if target else count - 1

        
        