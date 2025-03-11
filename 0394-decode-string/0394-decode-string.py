class Solution:
    def decodeString(self, s: str) -> str:
        def recu(i):
            ans = []
            while i < len(s):
                if s[i].isdigit():
                    digit = ""
                    while s[i] != '[':
                        digit += s[i]
                        i+=1
                    res,index = recu(i+1)
                    i = index
                    ans.append(res * int(digit))
                elif s[i] == ']':
                    return ''.join(ans),i+1
                else:
                    ans.append(s[i])
                    i+=1
            return ''.join(ans),i
        result , index = recu(0)
        return result
        



       

        



        