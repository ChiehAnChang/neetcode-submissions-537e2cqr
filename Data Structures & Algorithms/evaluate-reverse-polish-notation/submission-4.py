class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = set(['+', '-', '*', '/'])
        for each_token in tokens:
            if each_token not in s:
                stack.append(int(each_token))          # push int
            else:
                right = int(stack.pop())
                left = int(stack.pop())
            
                if each_token == '+':
                    stack.append(left + right)
                elif each_token == '-':
                    stack.append(left - right)
                elif each_token == '*':
                    stack.append(left * right)
                else:
                    divide = int(left / right)        # compute only when needed
                    stack.append(divide)
        return stack[-1]
