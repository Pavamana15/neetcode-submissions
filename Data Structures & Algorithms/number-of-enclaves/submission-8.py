class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        Enclaves = 0
        out = 0
        islanda_list = []
        

        

        
        def dfs(r, c,islands):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == 0
            ):
                return
            
            islands.append((r,c))
            visit.add((r,c))
            grid[r][c] = 0
            

            for dr, dc in directions:
                dfs(r + dr, c + dc, islands)

            return islands
        

        
                
                

        for r in range(1,ROWS-1):
            for c in range(1,COLS-1):
                if grid[r][c] == 1 and (r,c) not in visit:
                    print("The current position is :",r,c)
                    
                    res = dfs(r, c,[])
                    print("The return result from DFS is :", res)
                    islanda_list.append(res)
                    
        

        for island in islanda_list:
            count = 0
            for r,c in island:
                if r == 0 or r == ROWS-1 or c == 0 or c == COLS - 1:
                    count = 0

                    break
                else:
                    count += 1
            Enclaves += count


        return Enclaves


