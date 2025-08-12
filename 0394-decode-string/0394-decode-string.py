class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ''
        curr_num = 0
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr_str,curr_num))
                curr_str , curr_num = '' , 0
            elif ch == ']':
                prev_str , prev_num = stack.pop()
                curr_str = prev_str + (curr_str * prev_num)
            else:
                curr_str += ch
        return curr_str
            
