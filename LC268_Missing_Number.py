class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        c = sum(nums)

        count = 0
        for i in range(0, m+1):
            count += i
        if c < count:
            return count - c
        elif c == count:
            if 0 in nums:
                return m+1
            else:
                return 0
