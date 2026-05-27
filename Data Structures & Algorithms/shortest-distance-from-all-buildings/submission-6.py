class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        num_buildings = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        reach = [[0]*COLS for _ in range(ROWS)]

        visit = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if grid[r][c] == 1:
                    num_buildings += 1



        matrices = [
            [[0] * COLS for _ in range(ROWS)]
            for _ in range(num_buildings)]


        def bfs(r, c,k):
            q = deque()
            visit.add((r,c))
            q.append((r, c))
            dist = 1
            while q:
                for _ in range(len(q)): 
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = dr + row, dc + col
                        if (nr < 0 or nc < 0 or nr >= ROWS or
                            nc >= COLS or grid[nr][nc] == 2 or
                            (nr,nc) in visit or grid[nr][nc] == 1
                        ):
                            continue
                        q.append((nr, nc))
                        visit.add((nr,nc))
                        reach[nr][nc] += 1
                        
                        matrices[k][nr][nc] = dist
                dist += 1
            


        
        k = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    visit.clear()
                    bfs(r,c,k)
                    k += 1

        
        sum_matrix = [[0] * COLS for _ in range(ROWS)]

        for mat in matrices:
            for r in range(ROWS):
                for c in range(COLS):
                    sum_matrix[r][c] += mat[r][c]


        print("THe sum matrix is :", sum_matrix)

        min_val = min(
                    (
                        sum_matrix[r][c]
                        for r in range(ROWS)
                        for c in range(COLS)
                        if reach[r][c] == num_buildings
                    ),
                    default=-1
                )


        return min_val




         

        


        

         
#         building = []
#         distance_matrix = [[0] * len(grid[0]) for _ in range(len(grid))]

#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
                
#                 if grid[r][c] == 1:
#                     building.append((r, c))

#         ROWS, COLS = len(grid), len(grid[0])

#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]    

#         def shortest_distance(start,destination):
            
#             minHeap = [[0, start[0], start[1]]]  # [diff, row, col]
#             visit = set()
            

#             while minHeap:
#                 dist, r, c = heapq.heappop(minHeap)

#                 if (r, c) in visit:
#                     continue

#                 visit.add((r, c))

#                 if (r, c) == (destination[0], destination[1]):
#                     return dist

#                 for dr, dc in directions:
#                     newR, newC = r + dr, c + dc
#                     if (
#                         newR < 0 or newC < 0 or
#                         newR >= ROWS or newC >= COLS or
#                         (newR, newC) in visit or grid[newR][newC] == 2
#                     ):
#                         continue

#                     newDist = dist+1
#                     heapq.heappush(minHeap, [newDist, newR, newC])

#             return 0


#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == 0:
#                     for destination in building:
#                        distance_matrix[r][c] += shortest_distance((r,c),destination)

#         min_val = min(
#     (val for row in distance_matrix for val in row if val != 0 and val != float('inf')),
#     default=-1
# )



#         return min_val



        

