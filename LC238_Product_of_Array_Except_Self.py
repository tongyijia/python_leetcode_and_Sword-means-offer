class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        output = []

        left = [1 for i in range(n) ]
        right = [1 for i in range(n)]

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for j in range(n-2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]

        for i in range(n):
            output.append(left[i] * right[i])
        return output
