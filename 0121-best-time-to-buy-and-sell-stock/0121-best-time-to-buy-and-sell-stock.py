class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        lowest_price = prices[0]
        max_profit = 0

        for day in range(1, len(prices)):
            profit = prices[day] - lowest_price
            if profit > 0:
                max_profit = max(max_profit, profit)
            lowest_price = min(lowest_price, prices[day])

        return max_profit
