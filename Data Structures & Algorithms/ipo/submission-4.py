class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        current_capital = w
        


        
        

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

            if not minHeap:
                break


            profit, cap = heapq.heappop(minHeap)
            k -= 1
           
            current_capital += -profit
            

            
            print("The current capital is :", current_capital)


        return  current_capital


            

