class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # start = ~0
        # while left <= right:
        #     start &= left
        #     left +=1
        # print(start)

     
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        
        start = left << count
        return start