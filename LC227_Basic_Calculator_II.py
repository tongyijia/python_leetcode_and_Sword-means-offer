class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        hz = []
        stack = []

        priority = {
            '*': 1,
            '/': 1,
            '+': 0,
            '-': 0
        }

        operator = {
            '*' : lambda x,y : x * y,
            '/' : lambda x,y : x / y,
            '+' : lambda x,y : x + y,
            '-' : lambda x,y : x - y
        }

        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue

            if  48 <= ord(s[i]) <= 57:
                tmp = ""
                while i < len(s) and 48 <= ord(s[i]) <= 57:
                    tmp += s[i]
                    i += 1
                hz.append(tmp)

            elif len(stack) == 0:
                stack.append(s[i])
                i += 1
            else:
                while stack and priority[s[i]] <= priority[stack[-1]]:
                    hz.append(stack.pop())
                stack.append(s[i])
                i += 1

        while len(stack) > 0:
            hz.append(stack.pop())

        #print(hz)
        value = []
        for i in hz:
            if i not in ['+', '-', '*', '/']:
                value.append(int(i))
            else:
                n2 = value.pop()
                n1 = value.pop()
                value.append(operator[i](n1,n2))
        return value[0]
