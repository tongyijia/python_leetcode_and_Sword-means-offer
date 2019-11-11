class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pre = nums[len(nums)-k:]
        later = nums[:len(nums)-k]
        #print(pre,later)
        pre.extend(later)
       # print(pre)
        nums[:] = pre[:]
        #print(nums)
