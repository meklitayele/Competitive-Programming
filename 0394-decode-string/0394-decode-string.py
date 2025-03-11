class Solution:
    def decodeString(self, s: str) -> str:
        def rec(i):
            ans = []
            while i < len(s):
                if s[i].isdigit():
                    digit = ''
                    while s[i] != '[':
                        digit += s[i]
                        i += 1
                    result , index = rec(i+1)
                    i = index
                    ans.append(result * int(digit))
                elif s[i] == ']':
                    return ''.join(ans) , i+1
                else:
                    ans.append(s[i])
                    i+=1
            return ''.join(ans) , i
        ans , index = rec(0)
        return ans
        



       

        



        