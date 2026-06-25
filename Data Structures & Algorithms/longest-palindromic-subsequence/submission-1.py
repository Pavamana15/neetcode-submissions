class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # cache = {}
        
        # def dfs(left,right):
        #     if (left,right) in cache:
        #         return cache[(left,right)]
        #     if left == right:
                
        #         return 1
            
        #     if left > right:
        #         return 0

        #     res = 0

        #     if s[left] == s[right]:
        #         res = 2 + dfs(left+1,right-1)
        #     else:
        #         res =  max(dfs(left+1,right),dfs(left,right-1))

        #     cache[(left,right)] = res

        #     return cache[(left,right)]

        n = len(s)

        dp = [[0]*n for _ in range(n)]

        for j in  range(n):
            dp[j][j] = 1

        for left in range(n-2,-1,-1):
            for right in range(left+1,n):
                if s[left] == s[right]:
                    dp[left][right] = 2 + dp[left+1][right-1]
                else:
                    dp[left][right] = max(dp[left+1][right], dp[left][right-1])

        return dp[0][n-1]
            
                

            
            

        return dfs(0,len(s)-1)