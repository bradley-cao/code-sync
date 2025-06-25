class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        operators = {'+', '-', '*', '/'}

        while i < len(tokens):
            token = tokens[i]
            if token in operators:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == '+':
                    stack.append(num2 + num1)
                if token == '-':
                    stack.append(num2 - num1)
                if token == '*':
                    stack.append(num2 * num1)
                if token == '/':
                    stack.append(int(num2/num1))
            else:
                stack.append(tokens[i])
            i += 1
        return int(stack[0])