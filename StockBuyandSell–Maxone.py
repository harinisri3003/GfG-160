class Solution:
    def maximumProfit(self, prices):
        if not prices:  # If prices array is empty
            return 0
        
        min_price = float('inf')  # Initialize to a very large value
        max_profit = 0
        
        for price in prices:
            # Update minimum price
            min_price = min(min_price, price)
            # Calculate potential profit
            current_profit = price - min_price
            # Update maximum profit
            max_profit = max(max_profit, current_profit)
        
        return max_profit
