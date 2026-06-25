class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        
        def dfs(left,right):
            if (left,right) in cache:
                return cache[(left,right)]
            if left == right:
                
                return 1
            
            if left > right:
                return 0

            res = 0

            if s[left] == s[right]:
                res = 2 + dfs(left+1,right-1)
            else:
                res =  max(dfs(left+1,right),dfs(left,right-1))

            cache[(left,right)] = res

            return cache[(left,right)]
            
                

            
            

        return dfs(0,len(s)-1)