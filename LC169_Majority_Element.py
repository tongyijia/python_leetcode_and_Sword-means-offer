class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num = n // 2

        hash_table = {}

        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                hash_table[i] += 1

        for key,value in hash_table.items():
            if value > num:
                return key
        return 0
