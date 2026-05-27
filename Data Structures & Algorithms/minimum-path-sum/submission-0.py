class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for k in range(n-2,-1,-1):
            grid[m-1][k] +=  grid[m-1][k+1]

        for k in range(m-2,-1,-1):
            grid[k][n-1] +=  grid[k+1][n-1]


        
        

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                
                    grid[i][j] = min(grid[i][j] + grid[i + 1][j] , grid[i][j] + grid[i][j + 1])



                

        return grid[0][0]