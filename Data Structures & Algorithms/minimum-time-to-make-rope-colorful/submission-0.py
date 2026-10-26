class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        output = 0
        prev = [None,None]
        for i in range(len(colors)):
            if colors[i] == prev[0]:
                output += min(neededTime[i], prev[1])
                
                    
                    
                
                if neededTime[i] >= prev[1]:   
                    prev = [colors[i],neededTime[i]]
            else:
                prev = [colors[i],neededTime[i]]
                    
            
            
        
        return output
