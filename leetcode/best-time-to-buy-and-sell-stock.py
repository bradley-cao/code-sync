class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        maxPrice = 0
        for i in range(1, len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            maxPrice = max(maxPrice, prices[i] - buyPrice)
        return maxPrice