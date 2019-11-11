class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        #quick sort

        def partition(left, right, pivot_index):

            pivot = nums[pivot_index]
            nums[pivot_index],nums[left] = nums[left],nums[pivot_index]

            while left < right:
                while nums[right] >= pivot and left < right:
                    right -= 1
                nums[left] = nums[right]
                while nums[left] <= pivot and left < right:
                    left += 1
                nums[right] = nums[left]

            nums[left] = pivot
            return left

        def select(left, right, k_smallest):
            if left == right: return nums[left]

            #print(left,right)

            pivot_index = random.randint(left, right)

            pivot_index = partition(left, right, pivot_index)


            if pivot_index == k_smallest:
                return nums[k_smallest]
            elif pivot_index > k_smallest:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)



        return select(0, len(nums) - 1, len(nums) - k)
