class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2: return len(s)

        max_l = 0

        tmp = [s[0]]
        for i in range(1, len(s)):

            if s[i] not in tmp:
                tmp.append(s[i])
            else:
                tmp = tmp[tmp.index(s[i]) + 1:]
                tmp.append(s[i])

            if len(tmp) > max_l:
                max_l = len(tmp)

        return max_l
