class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = set(), set()
        servers = 0
        visit = set()
        max_servers = sum(sum(row) for row in grid)


        def dfs(r,c):
            nonlocal servers
            if r in ROWS:
                row_count = 0
            else:
                row_count = sum(grid[r])
                ROWS.add(r)

            if c in COLS:
                col_count  = 0
            else:
                col_count = sum(grid[r][c] for r in range(len(grid)))
                COLS.add(c)


            if row_count == 1 and col_count == 1:
                row_count = 0
                col_count = 1
            
            
            servers +=  row_count + col_count-1

            
                    
                

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    

        return servers

