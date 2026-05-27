class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        copy_image = [row[:] for row in image]
        ROWS = len(image)
        COLS = len(image[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()


        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or image[r][c] != image[sr][sc] or
                (r,c) in visit 
            ):
                return

            copy_image[r][c] = color
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        dfs(sr,sc)

        return copy_image





