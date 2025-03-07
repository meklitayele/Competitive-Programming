class Solution:
    def smallestSubsequence(self, s: str) -> str:
        store = set()
        stack = []
        lastIndex = {char : index for index, char in enumerate(s)}

        for index , char in enumerate(s):
            if char in store:
                continue  
            while stack and char < stack[-1] and lastIndex[stack[-1]]  > index:
                store.remove(stack.pop())

            stack.append(char)
            store.add(char)
        return "".join(stack)



        