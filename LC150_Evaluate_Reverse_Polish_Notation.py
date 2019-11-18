class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = ['+','-','*','/']
        stack = []

        for i in tokens:
            if i not in opr:
                stack.append(i)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == '+':
                    stack.append(int(num1 + num2))
                elif i == '-':
                    stack.append(int(num1 - num2))
                elif i == '*':
                    stack.append(int(num1 * num2))
                else:
                    stack.append(int(num1 / num2))
        return stack[-1]
