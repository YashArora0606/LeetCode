class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_previous_price = prices[0]
        profit = 0
        highest_price = 0
        for price in prices:
            lowest_previous_price = min(lowest_previous_price, price)
            profit = max(profit, price - lowest_previous_price)
        return profit