class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == 1 and n == 1 and obstacleGrid[m-1][n-1] == 1:
            return 0

        if m == 1 and n == 1 and obstacleGrid[m-1][n-1] == 0:
            return 1

        # memo = [[-1] * n for _ in range(m)]
        # def dfs(i, j):
        #     if i == (m - 1) and j == (n - 1):
        #         return 1
        #     if i >= m or j >= n or obstacleGrid[i][j]== 1:
        #         return 0
        #     if memo[i][j] != -1:
        #         return memo[i][j]

        #     memo[i][j] =  dfs(i, j + 1) + dfs(i + 1, j)
        #     return memo[i][j]

        # return dfs(0, 0)


        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
                

        return dp[0][0]