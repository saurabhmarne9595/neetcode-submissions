class Solution:
    def isValid(self, s: str) -> bool:
        dic =  {
            '(': ')',
            '{': '}',
            '[': ']',   
        }
        # []([{}])
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif stack:
                element = stack.pop()
                if char == dic[element]:
                    continue
                return False
            else:
                return False

        if(stack):
            return False
        return True
        