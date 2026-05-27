class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        current_capital = w
        total_profit = w


        if w < min(capital):
            return w
        

        Prof_Cap = []

        for a,b in zip(profits,capital):
            Prof_Cap.append([a,b])
        
        Prof_Cap.sort(key=lambda t: t[1])
        
        i=0
        


        while k != 0 :
            while i < len(Prof_Cap) and current_capital >= Prof_Cap[i][1]  :
                heapq.heappush(minHeap, [-Prof_Cap[i][0], Prof_Cap[i][1]])
                i += 1
            
            print("The i value is :",i)
            if minHeap:
                print("minHeap contents:", minHeap)
            else:
                print("minHeap is empty !!!!!!")

            profit, cap = heapq.heappop(minHeap)
            k -= 1
            total_profit += -profit
            current_capital += -profit
            

            print("The current total profit is :", total_profit)
            print("The current capital is :", current_capital)


        return total_profit


            

