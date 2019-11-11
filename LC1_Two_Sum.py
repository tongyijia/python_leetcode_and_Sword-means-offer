class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = []

        for i,a in enumerate(nums):
            if target - a  in nums and i != nums.index(target - a):
                res = [i, nums.index(target - a)]
                res.sort()
                return res
