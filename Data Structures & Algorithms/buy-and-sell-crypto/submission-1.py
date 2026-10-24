class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price_min = float("inf")
        for price in prices:
            if price < price_min:
                price_min = price
            elif price-price_min > profit:
                profit = price-price_min
        return profit