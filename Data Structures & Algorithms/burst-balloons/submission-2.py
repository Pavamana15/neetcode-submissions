class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def dfs(a):
            if not a:
                return 0
            
            key = tuple(a)
            if key in dp:
                return dp[key]
            
            max_val = 0
            for i in range(len(a)):
                pre = a[i-1] if i-1 >= 0 else 1
                post = a[i+1] if i+1 < len(a) else 1
                coins = pre * a[i] * post
                remaining = a[:i] + a[i+1:]
                max_val = max(max_val, coins + dfs(remaining))
            
            dp[key] = max_val
            return max_val

        return dfs(nums)

        
                

        