class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        store = set()
        lIndex = {char : index for index,char in enumerate (s)}
        
        for index , char  in enumerate(s):
            if char in store:
                continue
            while stack and stack[-1] > char and lIndex[stack[-1]] > index:
                store.remove(stack.pop())
           
            stack.append(char)
            store.add(char)
        return "".join(stack)
        


        
        