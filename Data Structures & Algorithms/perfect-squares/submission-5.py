class Solution:
    def numSquares(self, n: int) -> int:
        

        def perfect_squares_less_than(n):
            squares = []
            i = 1
            while i * i <= n:
                squares.append(i * i)
                i += 1
            return squares

        def perfect_squares(coins, amount):

        
            dp = [amount + 1] * (amount + 1)
            dp[0] = 0

            for a in range(1, amount + 1):
                print("The a value is :",a)
                for c in coins:

                    if a - c >= 0:
                        dp[a] = min(dp[a], 1 + dp[a - c])

            print("The dp is:",dp)
            return dp[amount] if dp[amount] != amount + 1 else -1

        
        nums = perfect_squares_less_than(n)
        print("The perfect square numbers list is :", nums)
        return perfect_squares(nums, n)









