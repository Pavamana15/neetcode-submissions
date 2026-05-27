class StockSpanner:

    def __init__(self):
        self.stock = []
        

    def next(self, price: int) -> int:
        span = 1
        
        # print("The present stock is :", self.stock)
        if self.stock:
            # print("The present stock is :", self.stock)
            while self.stock and self.stock[-1][0] <= price:
         
                span += self.stock[-1][1]
                self.stock.pop()

            
        
        self.stock.append([price,span])
        

        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)