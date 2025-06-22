class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif s[i] == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif s[i] == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            else:
                stack.append(s[i])
            i += 1
        return len(stack) == 0