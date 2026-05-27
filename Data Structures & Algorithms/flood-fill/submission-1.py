class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS = len(image)
        COLS = len(image[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        if image[sr][sc] == color:
            return image



        def dfs(r, c,org):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or image[r][c] != org 
                
            ):
                return

            image[r][c] = color
            
            for dr, dc in directions:
                dfs(r + dr, c + dc,org)

        dfs(sr,sc,image[sr][sc])

        return image





