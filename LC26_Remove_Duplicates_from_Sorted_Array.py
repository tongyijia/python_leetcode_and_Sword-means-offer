class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums: return 0
        i = 0
        j = 0

        while j < len(nums):
            if nums[i] != nums[j]:
                del nums[i+1:j]
                i += 1
                j = i
            elif j == len(nums) - 1 and i != j:
                del nums[i+1:]
            else:
                j += 1
        return len(nums)
