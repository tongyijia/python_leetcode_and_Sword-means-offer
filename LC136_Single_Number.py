class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}

        for i in nums:
            if hash_table.has_key(i):
                hash_table.pop(i)

            else:
                hash_table[i] = i

        return hash_table.values()[0]
