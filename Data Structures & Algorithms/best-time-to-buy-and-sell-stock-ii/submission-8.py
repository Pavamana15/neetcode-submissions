class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0

        while j < len(prices):
            if prices[j] - prices[i] >= 0:
                profit += prices[j] - prices[i]

            i += 1
            j += 1
        return profit


        # l, r = 0, 1
        # maxP = 0
        # cur_max = 0
        # max_list = []

        # while r < len(prices):
        #     if prices[l] < prices[r] and prices[r] > cur_max:
        #         cur_max = prices[r]
        #         profit = prices[r] - prices[l]
        #         maxP = max(maxP, profit)
                
        #     elif (prices[l] < prices[r] and prices[r] <= cur_max) or (prices[l] > prices[r] and prices[r] <= cur_max):
        #         max_list.append(maxP)
        #         print("The present maximum list are :", max_list)
        #         maxP = 0
        #         cur_max = 0
        #         l = r
        #     elif prices[l] > prices[r] and cur_max == 0:
        #         l += 1
        #     r += 1

        # max_list.append(prices[r-1] - prices[l])

        # print("The maximum list are:", max_list)
        # return sum(max_list)

                
        