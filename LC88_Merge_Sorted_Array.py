class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_copy =  nums1[:m]
        nums1[:] = []

        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums2[p2] <= nums1_copy[p1]:
                nums1.append(nums2[p2])
                p2 += 1
            else:
                nums1.append(nums1_copy[p1])
                p1 += 1

        if p1 != m:
            nums1.extend(nums1_copy[p1:])
        else:
            nums1.extend(nums2[p2:])
