class Solution:
    def maxArea(self, height: List[int]) -> int:

        #将指向较短线段的指针向较长线段那端移动一步
        max_area = min(height[0],height[-1]) * (len(height) - 1)

        i = 0; j = len(height) - 1
        while i != j:
            tmp = min(height[i],height[j]) * (j - i)
            if tmp > max_area:
                max_area = tmp
            else:
                if height[i] > height[j]:
                    j -= 1
                else:
                    i += 1
        return max_area
