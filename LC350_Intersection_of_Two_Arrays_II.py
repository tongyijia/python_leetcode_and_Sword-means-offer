class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        res = []

        if m > n :
            longer = nums1
            shorter = nums2
        else:
            longer = nums2
            shorter = nums1

        hash_table = dict()

        for i in longer:
            if hash_table.has_key(i):
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        for i in shorter:
            if hash_table.has_key(i):
                if hash_table[i] >= 1:
                    res.append(i)
                    hash_table[i] -= 1

        return res
