from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # Iterate over the prices list
        for i in range(1, len(prices)):
            # Add profit if the current price is greater than the previous day's price
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

