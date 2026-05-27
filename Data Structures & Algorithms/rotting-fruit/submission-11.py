import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        if all(1 not in sublist for sublist in grid):
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        Original_grid = grid.copy()
        res = []
        
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
                        grid[r][c] != 2 and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        
                        grid[r][c] =  grid[row][col]+1
                        


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                   print("The current (r,c) is :",r,c)
                   bfs(r, c)
                   res.append(copy.deepcopy(grid))
                   print("The result is :", res)
        
        if len(res) > 1:
            grid = [[min(a, b) for a, b in zip(matrix1, matrix2)] for matrix1, matrix2 in zip(res[0], res[1])]

        if any(1 in sublist for sublist in grid):
            return -1
        elif max(max(sublist) for sublist in grid if sublist) >2:
            result = max(max(sublist) for sublist in grid if sublist) - 2
            return result if result >0 else 0
        