class Solution:
    def climbStairs(self, n: int) -> int:
        steps = []

        steps.append(0)
        steps.append(1)
        steps.append(2)
        
        for i in range(3,n+1):
            steps.append(steps[i-1]+steps[i-2])

        return steps[n]
            
