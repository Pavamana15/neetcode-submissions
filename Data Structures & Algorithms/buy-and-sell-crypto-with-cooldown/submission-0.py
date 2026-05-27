class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]*(len(prices)+3)
        
        if len(prices) == 1:
            return 0

        for i in range(len(prices)-2,-1,-1):
            print("The current profit is:", profit)
            for j in range(i+1, len(prices)):

                profit[i] = max( (prices[j]-prices[i]) + profit[j+2], profit[i] )

            print("The  profit after update is:", profit)  


        return max(profit)            

        


        