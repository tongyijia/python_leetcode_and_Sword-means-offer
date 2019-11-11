class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0: return 0

        profit = 0
        cur_profit = 0
        min = prices[0]

        for i in prices:
            if i - min > cur_profit:
                cur_profit = i - min
            else:
                profit += cur_profit
                cur_profit = 0
                min = i

        profit += cur_profit
        return profit
