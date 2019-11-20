class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        min_n = float('inf')
        max_n = float('inf')

        for n in nums:
            if n < min_n:
                min_n = n
            elif min_n < n <= max_n:
                max_n = n
            elif n > max_n:
                return True
        return False
