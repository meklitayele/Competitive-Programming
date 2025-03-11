class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        temp = '0'
        
        def calc(temp,n,k):
            count = 0
            while count < n:
                curr = ''   
                ans = ''.join(['1' if char == '0' else '0' for char in temp])
                curr = '1' + ans[::-1] 
                # print(curr)
                temp += curr
                # print(temp)
                count += 1
            return temp
        # print(calc(temp,n,k))
        ans = str(calc(temp,n,k))
        return ans[k-1]
        # print(ans)



        