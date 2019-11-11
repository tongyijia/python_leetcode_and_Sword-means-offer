class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums: return 0
        dp = []

        for i in range(len(nums)):
            if i == 0:
                dp.append(nums[i])
            elif i == 1:
                dp.append(max(nums[0],nums[1]))
            else:
                dp.append(max(dp[i-1], dp[i-2] + nums[i]))
        #print(dp)

        return dp[len(nums) - 1]
