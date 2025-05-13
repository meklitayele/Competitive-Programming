class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            num = i
            while  num > 0:
                if num % 2 != 0:
                    count += 1
                num = num // 2
            res.append(count)
        return res
           


            


        