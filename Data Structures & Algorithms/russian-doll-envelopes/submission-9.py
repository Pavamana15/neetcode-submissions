class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: x[0] + x[1])
        
        
        dp = [1]*len(envelopes)
        

        for i in range(1, len(envelopes)):
            j = i
            while j:
                
                if envelopes[i][0] > envelopes[j-1][0] and envelopes[i][1] > envelopes[j-1][1]:

                    dp[i] = max(dp[j-1] + 1,dp[i])
                   
                   
                j -= 1
        
        return max(dp)

        