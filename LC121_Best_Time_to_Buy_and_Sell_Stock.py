class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0: return 0

        max_p = 0
        min = prices[0]

        for i in prices:
            if i < min :
                min = i

            if i - min > max_p:
                    max_p = i - min

        return max_p
