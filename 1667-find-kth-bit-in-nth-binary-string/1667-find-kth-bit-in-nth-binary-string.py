class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        temp = '0'
        
        def calc(temp):
            count = 0
            while count < n:
                curr = ''
                count += 1
                ans = ''.join(['1' if s == '0' else '0' for s in temp])
                # print(ans)
                curr = '1' + ans[::-1]
                temp += curr
                # print(temp)
            return temp
        ans = calc(temp)
        return ans[k-1]
        

          
            
        