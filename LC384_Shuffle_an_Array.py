class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        tmp = self.nums[:]
        n = len(tmp)
        for i in range(n):
            j = random.randint(i,n-1)
            tmp[i],tmp[j] = tmp[j],tmp[i]
        return tmp




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
