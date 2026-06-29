class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        max_side = 0

        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],
                        dp[i][j + 1],
                        dp[i + 1][j + 1]
                    )
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
                            


            
                

                


            

            

        