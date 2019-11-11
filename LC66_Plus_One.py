class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if len(digits) == 0: return False

        l1 = [0,1,2,3,4,5,6,7,8]
        l2 = [9]

        if digits[-1] in l1:
            digits[-1] += 1
            return digits
        elif digits[-1] in l2 and len(digits) == 1:
            return [1,0]
        else:
            digits[-1] = 0
            digits[:len(digits)-1] = self.plusOne(digits[:len(digits)-1])
            return digits
