class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x // 2 + 1


        while right > left :
            mid = left + (right - left ) // 2 + 1

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid
            else:
                right = mid - 1

        return left
