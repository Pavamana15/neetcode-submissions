class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        islands = [[0]*n for _ in range(m)]
        answer = []

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        current_islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= m or
                c >= n or grid[r][c] == 0
            ):
                return
            visit.add((r,c))
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for pos in positions:
            visit = set()
            current_islands  = 0
            # print("The current position to become land :", pos)
            islands[pos[0]][pos[1]] = 1

            # print("The current island is :", islands)
            grid = [row[:] for row in islands]

            # print("The copy of island is :",grid)
            for r in range(m):
                for c in range(n):
                    if islands[r][c] == 1 and (r,c) not in visit:
                        dfs(r, c)
                        current_islands += 1

            answer.append(current_islands)



        return answer
            
            

        