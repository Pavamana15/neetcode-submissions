class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str2

        dp = [['' for j in range(len(str2) + 1)]
                 for i in range(len(str1) + 1)]
        for i in range(len(str1)):
            dp[i][-1] = str1[i:]

        for i in range(len(str2)):
            dp[-1][i] = str2[i:]

        for i in range(len(str1) - 1, -1, -1):
            for j in range(len(str2) - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = str1[i] + dp[i + 1][j + 1]
                else:
                    if len(str2[j] + dp[i][j + 1]) < len(str1[i] + dp[i + 1][j]):
                        dp[i][j] = str2[j] + dp[i][j + 1]
                    else:
                        dp[i][j] = str1[i] + dp[i + 1][j]
                    
        
        return dp[0][0]

        
        
        


        