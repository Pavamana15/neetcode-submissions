class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = []
        for i,price in enumerate(prices):
            if any(x > price for x in prices[i+1:]):
                maxProfit.append(max(prices[i+1:]) - price)
            else:
                continue

        return max(maxProfit) if maxProfit  else 0

