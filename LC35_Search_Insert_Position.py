class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if len(nums) == 0: return 0

        if target in nums:
            return nums.index(target)
        elif nums[0] > target:
            nums.insert(0,target)
            return 0
        else:
            for i in range(1,len(nums)):
                if nums[i-1] < target and nums[i] > target:
                    nums.insert(i,target)
                    return i

        nums.append(target)
        return len(nums)-1
