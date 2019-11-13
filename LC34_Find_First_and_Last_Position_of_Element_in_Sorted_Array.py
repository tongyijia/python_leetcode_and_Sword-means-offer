class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarysearch(target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    return mid
            return -1

        res = [-1, -1]
        if len(nums) == 0: return [-1,-1]
        if len(nums) == 1:
            if target == nums[0]:
                return [0,0]
            else:
                return [-1,-1]


        index = binarysearch(target)
        if index == -1:
            return res
        else:
            while index > -1 and nums[index] == target:
                index -= 1
            res[0] = index + 1
            index += 1
            while index < len(nums) and nums[index] == target:
                index += 1
            res[1] = index - 1
        return res
