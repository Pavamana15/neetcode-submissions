class Solution:

    def __init__(self, w: list[int]):
        self.w = w
        

        # for i in range(len(self.w)):
        #     self.probabilities[i] = self.w[i] / sum(self.w)
        

    def pickIndex(self) -> int:
        return random.choices(range(len(self.w)), weights=self.w, k=1)[0]
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()