class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # start = ~0
        # while left <= right:
        #     start &= left
        #     left +=1
        # print(start)

        while right > left:
            right &= (right-1)
        return right

     