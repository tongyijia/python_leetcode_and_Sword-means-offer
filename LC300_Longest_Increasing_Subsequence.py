class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums: return 0
        dp = [1]
        for i in range(1, len(nums)):
            max_l = 1
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > max_l:
                    max_l = dp[j] + 1
            dp.append(max_l)
        return max(dp)


       
