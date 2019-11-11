class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        temp = nums[:]
        temp.sort()
        max = temp[-1]
        return nums.index(max)
