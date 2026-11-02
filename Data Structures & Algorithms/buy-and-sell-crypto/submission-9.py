class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        profit_max = 0

        for i in range(len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
            
            price = prices[i] - curr_min
            profit_max = max(price, profit_max)
        return profit_max




