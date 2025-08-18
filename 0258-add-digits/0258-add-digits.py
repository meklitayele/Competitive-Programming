class Solution:
    def addDigits(self, num: int) -> int:
        def calc(number):
            total = 0
            if len(str(number)) == 1:
                return int(number)
            for n in number:
                total += int(n)
            total = str(total)
            return calc(total)

        num = str(num)
        return int(calc(num))

           




            


        