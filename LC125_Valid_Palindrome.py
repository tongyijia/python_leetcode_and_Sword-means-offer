class Solution:
    def isPalindrome(self, s: str) -> bool:

        queue = []

        for i in s:
            if ord(i) >= 97 and ord(i) <= 122:
                queue.append(i)
            elif ord(i) >= 65 and ord(i) <= 90:
                queue.append(chr(ord(i) + 32))
            elif ord(i) >= 48 and ord(i) <= 57:
                queue.append(i)
        if len(queue) == 1: return True

        while len(queue) > 1:
            #print(queue)
            if queue[0] == queue[-1]:
                queue.pop(0)
                queue.pop()
            else:
                return False

        return True
