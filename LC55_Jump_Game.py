class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 0: return False

        lastpos = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= lastpos:
                lastpos = i

        return lastpos == 0
