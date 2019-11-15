class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        table = {}
        for i in nums:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1
        i = 0
        while i < len(nums):
            if 0 in table:
                for j in range(table[0]):
                    nums[i] = 0
                    i += 1
            if 1 in table:
                for j in range(table[1]):
                    nums[i] = 1
                    i += 1
            if 2 in table:
                for j in range(table[2]):
                    nums[i] = 2
                    i += 1
