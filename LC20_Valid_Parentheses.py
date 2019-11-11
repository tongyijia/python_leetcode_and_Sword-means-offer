class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0 : return True
        if len(s) % 2 != 0: return False

        stack = []

        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            elif i in [")", "]", "}"] and len(stack) != 0:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
