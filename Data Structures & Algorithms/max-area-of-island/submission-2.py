class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        regions = []
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, subislands):
            
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return subislands

            visit.add((r, c))
            
            subislands.append((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, subislands)

            return subislands

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    islands += 1
                    subregions = dfs(r, c, [])
                    regions.append(subregions)

        
        
        print("The set of islands are :", regions)
        return max(len(region) for region in regions) if  regions else 0