class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                # 满足分割条件，进行分割
                return max(self.longestSubstring(t, k) for t in s.split(c))
        # 如果每个字符出现的次数均不小于k，则返回当前字符串的长度
        return len(s)
