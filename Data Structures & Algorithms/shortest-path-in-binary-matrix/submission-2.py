class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],[-1,-1],[-1,1],[1,1],[1,-1]]
        N = len(grid)
        islands = 0

        res = 1

        if grid[0][0]:
            return -1

        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N

        visit = set()
        visit.add((0,0))

        def bfs():
            res, q = 1, deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit or grid[curR][curC]:
                            continue
                        if not grid[curR][curC] and curR == N-1 and curC == N-1:
                            return res +1
                        q.append((curR, curC))
                        visit.add((curR, curC))
                res += 1

            return -1



        
        return bfs()