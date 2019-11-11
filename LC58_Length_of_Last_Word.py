class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if len(s) == 0: return 0

        count = 0
        flag = 0
        for i in s[::-1]:
            if i == " ":
                if flag == 1:
                    return count
            elif flag == 1:
                count += 1
            else:
                flag = 1
                count += 1

        return count
