class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        Original_grid = grid.copy()
        
        def bfs(r,c ):
            visit.clear()
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            print("The visit set are:", visit)

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if( r in range(rows) and
                        c in range(cols) and
                        grid[r][c] > 0 and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        
                        grid[r][c] = min( grid[r][c], grid[row][col]+1)
                        


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                   print("The current (r,c) is :",r,c)
                   bfs(r, c)


        return None
                    
        
        
        
        
        