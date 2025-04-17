class Solution:
    def simplifyPath(self, path: str) -> str:
        value = path.split('/')
        stack = []
        
        for val in value:
            if val == "" or val ==".":
                continue
            if val == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(val)
        return '/' + '/'.join(stack)

        
        