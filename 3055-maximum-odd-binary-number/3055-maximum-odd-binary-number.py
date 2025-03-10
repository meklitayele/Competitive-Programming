class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        store = Counter(s)
        res = []
        one = store['1'] - 1
        zero = store['0']
        res.append(one * '1')
        res.append(zero * '0')
        res.append('1')
        # print(one)
        # print(zero)
        ans = ''.join(res)
        return str(ans)

        
        

        