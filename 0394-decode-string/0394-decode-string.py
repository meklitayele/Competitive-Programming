class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ''
        curr_num = 0
        n = len(s)

        for i in range(n):
            curr = s[i]
            if curr.isdigit():
                curr_num = curr_num * 10 + int(curr)
            elif curr == '[':
                stack.append((curr_str,curr_num))
                curr_str , curr_num = '' , 0
            elif curr == ']':
                prev_str , prev_num = stack.pop()
                curr_str = prev_str + prev_num * curr_str
            else:
                curr_str += curr
        return curr_str

        