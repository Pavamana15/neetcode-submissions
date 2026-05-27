class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        visit = set()
        minH = [[0, 0, 0]]  
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        effort = 0

        
        while minH:
            t, r, c = heapq.heappop(minH)

            if (r, c) in visit:
                continue
            visit.add((r,c))
            if r == ROWS - 1 and c == COLS - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR >= ROWS or neiC >= COLS or
                    (neiR, neiC) in visit
                ):
                    continue
                
                heapq.heappush(minH, [max(abs(heights[neiR][neiC]-heights[r][c]) , t), neiR, neiC])

            
        return 0