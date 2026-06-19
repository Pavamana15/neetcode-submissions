class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        cache = {}

        def dfs(r1,c1,r2):
            if (r1,c1,r2) in cache:
                return cache[(r1,c1,r2)]
            c2 = r1 + c1 - r2

            if r1 <0 or r1 >= ROWS or c1<0 or c1 >= COLS or grid[r1][c1]== -1:
                return -float('inf')
            if  r2 <0 or r2 >= ROWS or c2<0 or c2 >= COLS or grid[r2][c2]== -1:
                return -float('inf')

            if r1 == ROWS-1 and c1 == COLS -1 :
                
                return grid[r1][c1]


            
            count = 0
            if r1 == r2 and c1 == c2:
                count += grid[r1][c1]
            else:
                count += grid[r1][c1] + grid[r2][c2]
            

            best = max(
                        dfs(r1+1, c1,   r2+1),   # down, down
                        dfs(r1+1, c1,   r2),     # down, right
                        dfs(r1,   c1+1, r2+1),   # right, down
                        dfs(r1,   c1+1, r2)      # right, right
                    )

            


            if best == -float('inf'):
                cache[(r1,c1,r2)] = -float('inf')
                return -float('inf')

            cache[(r1,c1,r2)] = count + best

            return count + best

    

        
       

        return max(dfs(0,0,0),0)

        


            

            

        