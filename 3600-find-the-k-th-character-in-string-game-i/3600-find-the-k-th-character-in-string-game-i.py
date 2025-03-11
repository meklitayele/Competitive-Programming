class Solution:
    def kthCharacter(self, k: int) -> str:
        def generate(temp):
            if len(temp) >= k:
                return temp
            curr = ''.join(chr(ord(char) + 1) if char != 'z' else 'a' for char in temp)
            return generate(temp + curr)
        
        ans = generate('a')
        return ans[k-1]


        


